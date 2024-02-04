import csv
import Hospital
import Resident

hospitals = []
residents = []

# Read CSV and input info into hospitals and residents
csv_file = './input.csv'
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    onResidents = False
    for row in csv_reader:
        if not row:
            onResidents = True
            continue

        if onResidents:
            resident = Resident.Resident()
            resident.set_name(row[0])
            resident_preferences = row[1:]
            for preference in resident_preferences:
                resident.add_preference(preference)
            residents.append(resident)
        else:
            hospital = Hospital.Hospital()
            hospital.set_name(row[0])
            hospital.set_slots(row[1])
            hospital_preferences = row[2:]
            for preference in hospital_preferences:
                hospital.add_preference(preference)
            hospitals.append(hospital)

for hospital in hospitals:
    output_string = 'Hospital: {}, Slots: {}, Preferences: {}'.format(hospital.name,
                                                                      hospital.slots, hospital.preferences)
    print(output_string)

print('')

for resident in residents:
    output_string = 'Resident: {}, Preferences: {}'.format(resident.name, resident.preferences)
    print(output_string)

# Gale Shapley Algorithm
print("")
matching = []
res_num = 0
hos_num = 0
while hos_num < len(hospitals) and len(hospitals[hos_num].preferences) > int(hospitals[hos_num].get_slots()):
    cur_resident = hospitals[hos_num].preferences[res_num]

    print("Checking if {} {} and {} {} match".format(hospitals[hos_num].name, hos_num, cur_resident, res_num))

    if any(x for x in residents if x.name == cur_resident):
        cur_hospital = hospitals[hos_num]

        print("Match Found")
        print(cur_hospital.get_name(), cur_resident)
        print("")

        # getting an error from this. getting boned rn frfr
        # Remember that cur_resident is a string. Search residents with get_name to find a match
        for resident in residents:
            if resident.get_name() == cur_resident:
                residents.remove(resident)
                break
        # The code now works past this until Chicago tries to take Xavier, but he is already taken
        matching.append((cur_hospital, cur_resident))  # Append after the resident is removed incase it breaks
        # Also feel free to open an issue if something happens again
        hos_num += 1
        res_num = 0
    elif (any(x for x in residents if x.name == cur_resident) and residents[residents.index(cur_resident)].preferences.index(matching[0][0].get_name())
          < residents[residents.index(cur_resident)].preferences.index(hospitals[hos_num])):
        cur_hospital = hospitals[hos_num]
        matching.append((cur_hospital, cur_resident))
        residents.remove(cur_resident)
        hos_num += 1
        res_num = 0

        for (hospital, resident) in matching:
            print("Match Replaced")
            print(hospital.name, resident.name)
    else:
        res_num += 1


print("")
for (hospital, resident) in matching:
    print(hospital.name, resident)
# while len(residents) > 0:
