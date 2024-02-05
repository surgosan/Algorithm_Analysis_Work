class Hospital:
    name = ''
    slots = 0
    preferences = []
    currently_matched = []

    # Hospital Initialization
    def __init__(self):
        self.name = ''
        self.slots = 0
        self.preferences = []
        self.currently_matched = []

    # Set Hospital's Name
    def set_name(self, name):
        self.name = name

    # Set Amount of Hospital Slots
    def set_slots(self, number_of_slots):
        self.slots = number_of_slots

    # Adds a resident to the currently_matched array
    def set_match(self, resident):
        self.currently_matched.append(resident)

    # Adds a resident to the preferences array
    def add_preference(self, resident):
        # Make sure to add the name using getName() instead of the object
        self.preferences.append(resident)

    # if the hospital has their maximum matches:
    # Adds a resident to the currently_matched array if they are more desired than a current match
    # Does nothing if the resident is less desired than a current match
    # if hospital doesn't have max matches just add the resident to the currently_matched array
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

    # Return the name of the hospital
    def get_name(self):
        return self.name

    # Return the number of slots the hospital has
    def get_slots(self):
        return self.slots

    # Return a string of preferred residents
    def get_preferences(self):
        name_list = ''
        for preference in self.preferences:
            if not name_list:
                name_list = preference.get_name()
            else:
                name_list += ', ' + preference.get_name()
        return name_list

    # Return the residents currently matched with
    def get_currently_matched(self):
        return self.currently_matched

    # Prints out the name of the hospital
    def print_name(self):
        print(self.name)

    # Prints out the amount of slots
    def print_slots(self):
        print(self.slots)

    # Prints out the names of preferred residents
    def print_preferences(self):
        print(self.preferences[0].get_name())

    # prints out the names of matched residents
    def print_currently_matched(self):
        print(self.currently_matched)
