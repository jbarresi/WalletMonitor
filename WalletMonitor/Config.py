class Config:
    # Constructor with default values
    def __init__(self, wallets_to_watch=[], check_interval_in_seconds=60, notification_sound_path=""):
        self.wallets_to_watch = wallets_to_watch
        self.check_interval_in_seconds = check_interval_in_seconds
        self.notification_sound_path = notification_sound_path

    # Get the array of wallets to watch Array[String]
    def get_wallets_to_watch(self):
        return self.wallets_to_watch

    # Get the check interval value (int)
    def get_check_interval_in_seconds(self):
        return self.check_interval_in_seconds

    # Get the notification sound path (string)
    def get_notification_sound_path(self):
        return self.notification_sound_path
