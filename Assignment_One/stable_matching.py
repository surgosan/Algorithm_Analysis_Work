import csv
import Hospital
import Resident

hospitals = []
residents = []
matches = []

csv_file = './input.csv'
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    onResidents = False
    for row in csv_reader:
        if not row:
            onResidents = True
            continue

        if not onResidents:
            hospital = Hospital.Hospital()
            hospital.set_name(row[0])
            hospital.set_slots(row[1])
            hospital_preferences = row[2:]
            for preference in hospital_preferences:
                hospital.add_preference(preference)
            hospitals.append(hospital)
        else:
            resident = Resident.Resident()
            resident.set_name(row[0])
            resident_preferences = row[1:]
            for preference in resident_preferences:
                resident.add_preference(preference)
            residents.append(resident)

for hospital in hospitals:
    output_string = 'Hospital: {}, Slots: {}, Preferences: {}'.format(hospital.name,
                                                                      hospital.slots, hospital.preferences)
    print(output_string)

for resident in residents:
    output_string = 'Resident: {}, Preferences: {}'.format(resident.name, resident.preferences)

h1 = Hospital.Hospital()
r1 = Resident.Resident()
r1.set_name('guy')

r2 = Resident.Resident()
r2.set_name('guy2')

r3 = Resident.Resident()
r3.set_name('guy3')

h1.set_name("Atlanta")
h1.set_slots(2)
hospital_preference_list = [r1, r2, r3]
for name in hospital_preference_list:
    h1.add_preference(name)

# h1.print_preferences()
# h1.print_slots()
# print(h1.get_preferences())
