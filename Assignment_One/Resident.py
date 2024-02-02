
class Resident:
    name = ""
    preferences = []
    current_match = None

    def __init__(self):
        self.name = ''
        self.preferences = []
        self.current_match = None

    def set_name(self, name):
        self.name = name

    def add_preference(self, preference):
        self.preferences.append(preference)

    def get_name(self):
        return self.name

    def get_preferences(self):
        return self.preferences

    def print_name(self):
        print(self.name)

    def print_preferences(self):
        for preference in self.preferences:
            name = preference.get_name()
            print(name)

