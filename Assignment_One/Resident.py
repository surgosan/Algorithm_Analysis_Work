
class Resident:
    name = ""
    preferences = []
    current_match = None

    # Resident Initialization
    def __init__(self):
        self.name = ''
        self.preferences = []
        self.current_match = None

    # Sets the name of resident
    def set_name(self, name):
        self.name = name

    # Adds a hospital to the preferences array
    def add_preference(self, preference):
        self.preferences.append(preference)

    # Sets a hospital to be the resident's current_match
    def set_match(self, hospital):
        self.current_match = hospital

    # Returns the resident's name
    def get_name(self):
        return self.name

    # Return the preferred hospitals
    def get_preferences(self):
        return self.preferences

    # Returns the hospital currently matched
    def get_current_match(self):
        return self.current_match

    # Prints out the resident's name
    def print_name(self):
        print(self.name)

    # Prints out the name of preferred hospitals
    def print_preferences(self):
        for preference in self.preferences:
            name = preference.get_name()
            print(name)

