# src/core/environment.py
class Environment:
    def __init__(self):
        self.shared_data = {}  # Example: a simple dictionary

    def get_data(self, key):
        return self.shared_data.get(key)

    def set_data(self, key, value):
        self.shared_data[key] = value