class Hospital:
    name = ''
    slots = 0
    preferences = []
    currently_matched = []

    def __init__(self):
        self.name = ''
        self.slots = ''
        self.preferences = []
        self.currently_matched = []

    def set_name(self, name):
        self.name = name

    def set_slots(self, number_of_slots):
        self.slots = number_of_slots

    def set_match(self, resident):
        self.currently_matched.append(resident)

    def add_preference(self, resident):
        # Make sure to add the name using getName() instead of the object
        self.preferences.append(resident)

    def check_match(self, resident):
        if len(self.currently_matched) >= self.slots:
            for match in self.currently_matched:
                if self.preferences.index(self.currently_matched[match.get_name()]) < self.preferences.index(resident)\
                        and resident.preferences.index(resident.current_match) < resident.preferences.index(self):
                    return
                else:
                    self.currently_matched[match] = resident
        else:
            self.currently_matched.append(resident)

    def get_name(self):
        return self.name

    def get_slots(self):
        return self.slots

    def get_preferences(self):
        """name_list = ''
        for preference in self.preferences:
            if not name_list:
                name_list = preference.get_name()
            else:
                name_list += ', ' + preference.get_name()"""
        return self.preferences

    def get_currently_matched(self):
        return self.currently_matched

    def print_name(self):
        print(self.name)

    def print_slots(self):
        print(self.slots)

    def print_preferences(self):
        print(self.preferences[0].get_name())

    def print_currently_matched(self):
        print(self.currently_matched)
