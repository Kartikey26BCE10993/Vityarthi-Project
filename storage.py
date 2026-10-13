import json
import os
from models import Transaction, UserSettings

class StorageHandler:
    """Handles persistent reading and writing to JSON data files safely in the project directory."""

    def __init__(self, data_file="data.json", settings_file="settings.json"):
        # Anchor paths to the directory where storage.py resides
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(base_dir, data_file)
        self.settings_file = os.path.join(base_dir, settings_file)

    def load_transactions(self):
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Transaction.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"[Warning] Failed to load transaction data: {e}")
            return []

    def save_transactions(self, transactions):
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump([item.to_dict() for item in transactions], file, indent=4)
        except IOError as e:
            print(f"[Error] Save transaction failed: {e}")

    def load_settings(self):
        if not os.path.exists(self.settings_file):
            return UserSettings(daily_limit=0.0)
        try:
            with open(self.settings_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return UserSettings.from_dict(data)
        except (json.JSONDecodeError, IOError):
            return UserSettings(daily_limit=0.0)

    def save_settings(self, settings):
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as file:
                json.dump(settings.to_dict(), file, indent=4)
        except IOError as e:
            print(f"[Error] Save settings failed: {e}")