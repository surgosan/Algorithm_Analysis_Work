class Hospital:
    slots = 0
    preferences = []
    currently_matched = None

    def add_resident(self, resident):
        self.preferences.append(resident)

    def set_slots(self, number_of_slots):
        self.slots = number_of_slots

