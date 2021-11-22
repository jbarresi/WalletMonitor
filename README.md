# WalletMonitor
Python based Crypto wallet monitor that runs as a console app. 

This runs in your console and will play a sound when a change is detected.

This utilizes the OpenSea NFT API (Available here: https://docs.opensea.io/reference/api-overview). This does not utilize an API key and as such is rate limited. If you are going to making this call outside this rate please consider modifying the code to use an API key and apply for one with OpenSea.

This is provided as is with no promise of warranty or commitment to bug fixes. 

***Note:*** There is a runtime error that will appear every time you restart the application. This is a known issue with the PyDub library at the time of writing this application. No idea if it will ever be fixed.

## Prerequisites
In order to run this you will need the following modules installed:
 - PyDub `pip install pydub`
 - SimpleAudio `pip install simpleaudio`
 - Requests `pip install requests`


## Configuring the Application
The application uses a config.json that is loaded at first run you can find this in `config/config.json` and looks like the following:

```
{
  "walletsToWatch": ["your_wallet_address_here", "your_other_wallet_address_here"],
  "checkIntervalInSeconds": 600,
  "notificationSound": "resources/hey-ringtone.wav"
}

```
Some things to note about the config file:
- This can accomodate as many wallet addresses as you want as long as they are added (comma separated as strings) to the JSON array for the element of the config file. 
- You can also change the check interval, by default this is set to 10 minutes, you can set this to your heart's desire but as a recommendation I would go no lower than half this.
- You can change the notification sound to whatever you'd like but it **MUST** be a .wav file. I would also recommend putting it in the `resources` directory and changing the file name to the audio file you want.

## Acknolwedgements
I need to give the following call outs for both the idea and technological contributions as they are well deserved:
- hahaschool#0933 from the Big Head Club discord, his original watcher was an inspiration for mine. His GitHub is: https://github.com/hahaschool
- OpenSea fot their NFT API, this wouldn't actually work if it wasn't for their API existing. It lives here: https://docs.opensea.io/reference/api-overview1
