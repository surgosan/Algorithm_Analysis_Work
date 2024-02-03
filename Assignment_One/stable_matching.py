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
while res_num < len(residents):
    cur_resident = hospitals[hos_num].get_preferences()[res_num]

    print("{}, resNum: {}".format(cur_resident, res_num))
    if cur_resident.current_match is None and cur_resident in hospitals[hos_num].preferences:
        cur_hospital = hospitals[hos_num]
        matching.append((cur_hospital, cur_resident))
        cur_hospital.set_match(cur_resident)
        cur_resident.set_match(cur_hospital)
        res_num += 1

        for (hospital, resident) in matching:
            print("Match Found")
            print(hospital.name, resident.name)
    elif cur_resident.current_match is not None and cur_resident.get_preferences().index(
            cur_resident.get_current_match().name) \
            < cur_resident.get_preferences().index(hospitals[hos_num]):
        cur_hospital = hospitals[hos_num]
        matching.remove((cur_resident.get_current_match(), cur_resident))
        matching.append((cur_hospital, cur_resident))
        cur_hospital.set_match(cur_resident)
        cur_resident.set_match(cur_hospital)
        res_num += 1

        for (hospital, resident) in matching:
            print("Match Replaced")
            print(hospital.name, resident.name)
    else:
        res_num += 1
        hos_num += 1

    if hos_num == len(hospitals):
        hos_num = 0

print("")
for (hospital, resident) in matching:
    print(hospital.name, resident.name)
# while len(residents) > 0:
