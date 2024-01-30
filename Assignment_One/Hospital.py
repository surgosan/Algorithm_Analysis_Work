class Hospital:
    name = ''
    slots = 0
    preferences = []
    currently_matched = []

    def set_name(self, name):
        self.name = name

    def set_slots(self, number_of_slots):
        self.slots = number_of_slots

    def add_preference(self, resident):
        # Make sure to add the name using getName() instead of the object
        self.preferences.append(resident)

    def check_match(self, resident):
        if len(self.currently_matched) >= self.slots:
            for match in self.currently_matched:
                if self.preferences.index(self.currently_matched[match]) < self.preferences.index(resident):
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
        return self.preferences

    def get_currently_matched(self):
        return self.currently_matched

    def print_slots(self):
        print(self.slots)
