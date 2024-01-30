class Residents:
    name = ""
    preferences = []

    def set_name(self, name):
        self.name = name

    def add_preference(self, preference):
        self.preferences.append(preference)

    def get_name(self):
        return self.name

    def get_preferences(self):
        return self.preferences


