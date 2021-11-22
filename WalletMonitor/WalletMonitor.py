import json
import time
import requests
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
from Config import Config


# Loads settings from config.json. Returns config object
def load_config():
    # Set success to false by default, let it stay false in the event there's a problem loading
    # the config file.
    config = None

    # open the config gile and load to variables
    with open('config/config.json') as config_file:
        data = json.load(config_file)
        wallet_list = data['walletsToWatch']
        check_interval_in_seconds = data['checkIntervalInSeconds']
        notification_sound_file_location = data['notificationSound']
        config = Config(wallet_list, check_interval_in_seconds, notification_sound_file_location)

    return config


# Plays an alert sound. This works with WAV and MP3 files.
def play_alarm(filepath):
    audio_file = AudioSegment.from_wav(filepath)
    play(audio_file)


# Calls the open sea api for a given wallet to get the current number of assets in it
def call_opensea_api_for_wallet_asset_count_update(wallet_addr):
    url = f'https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&owner={wallet_addr}'

    # this mechanic will keep looping until we break (basically to make sure we get a good response
    while True:
        print(f'{datetime.now()} - Attempting to call OpenSea for wallet: {wallet_addr}')
        response = requests.request("GET", url)
        if response.ok:
            print(f'{datetime.now()} - Asset count updated for wallet: {wallet_addr}')
            return len(response.json()['assets'])


# Main function that runs the wallet monitor
if __name__ == '__main__':
    print('Wallet Monitor Starting')

    # When we start up we're not going to do a check we're going to grab the current
    # asset count per wallet so we need a flag to tell us so
    is_first_run = True

    # Store previous results of the check
    wallet_asset_counts = {}

    # Grabs everything from the config file to set up the app
    conf = load_config()

    # Sentry loop to keep the monitor running
    while True:
        for current_wallet in conf.wallets_to_watch:
            # Get the current count of assets in the wallet
            current_asset_count = call_opensea_api_for_wallet_asset_count_update(current_wallet)
            # If this is the first run we're just going to update our dictionary with what we have
            if is_first_run:
                wallet_asset_counts[current_wallet] = current_asset_count
                continue

            # Perform our regular check, just see if the number of assets is the same as last time
            if current_asset_count != wallet_asset_counts[current_wallet]:
                # If number of assets isn't the same as last time, print to the console and play our notification sound
                play_alarm(conf.notification_sound_path)
                alert_message = f'{datetime.now()} - Number of assets in wallet {current_wallet}! Was: {wallet_asset_counts[current_wallet]}. Now: {current_asset_count}. You may want to go check your wallet'
                print(alert_message)

        # If we get this far and it's still our first run we've succeeded, set the first run flag to stop
        is_first_run = False
        # Sleep for our configured amount of time
        time.sleep(conf.check_interval_in_seconds)
