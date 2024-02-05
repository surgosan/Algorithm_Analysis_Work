import csv
import Hospital
import Resident

# Initialize lists to input hospital and resident objects
hospitals = []
residents = []

# Parse CSV, create objects, and input into hospitals and residents
csv_file = './data_set_two.csv'
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    onResidents = False
    for row in csv_reader:
        if not row:
            onResidents = True
            continue

        if onResidents:
            resident = Resident.Resident()
            resident.set_name(row[0].replace(" ", "").lower())
            resident_preferences = row[1:]
            for preference in resident_preferences:
                resident.add_preference(preference.replace(" ", "").lower())
            residents.append(resident)
        else:
            hospital = Hospital.Hospital()
            hospital.set_name(row[0].replace(" ", "").lower())
            hospital.set_slots(row[1])
            hospital_preferences = row[2:]
            for preference in hospital_preferences:
                hospital.add_preference(preference.replace(" ", "").lower())
            hospitals.append(hospital)
# Print out hospital's name, slot amount, and preferences from greatest to least
for hospital in hospitals:
    output_string = 'Hospital: {}, Slots: {}, Preferences: {}'.format(hospital.name,
                                                                      hospital.slots, hospital.preferences)
    print(output_string)

print('')
# Print out resident's name and preferences from greatest to least
for resident in residents:
    output_string = 'Resident: {}, Preferences: {}'.format(resident.name, resident.preferences)
    print(output_string)

# Modified Gale Shapley Algorithm
print("")
matching = []
res_num = 0
hos_num = 0
current_iteration = 0
while hos_num < len(hospitals):
    # Print out current iteration
    current_iteration = current_iteration + 1
    print("{}:".format(current_iteration))
    # Update current_resident's info (name and index in Residents)
    current_preference_name = hospitals[hos_num].preferences[res_num]
    current_preference_index = None
    for resident in residents:
        if resident.name == current_preference_name:
            current_preference_index = residents.index(resident)
            break
    # Announcing next match attempt
    print(
        "Checking if {} and {} match".format(hospitals[hos_num].name.capitalize(),
                                             current_preference_name.capitalize()))

    # If the preference is unmatched
    if any(x for x in residents if x.name == current_preference_name and x.current_match is None):
        cur_hospital = hospitals[hos_num]
        print("{} matches with {} who was previously unmatched\n".format(cur_hospital.get_name().capitalize(),
                                                                         current_preference_name.capitalize()))
        for resident in residents:
            if resident.get_name() == current_preference_name:
                resident.current_match = cur_hospital.get_name()
                break
        matching.append((cur_hospital, current_preference_name))
        cur_hospital.currently_matched.append(current_preference_name)
        if len(hospitals[hos_num].currently_matched) >= int(hospitals[hos_num].get_slots()):
            hos_num += 1
            if not hos_num >= len(hospitals):
                cur_hospital = hospitals[hos_num]
            res_num = 0

    # If the current hospital and resident is already matched
    elif any(x for x in matching if x[0].get_name() == hospitals[hos_num].get_name() and
                                    x[1] == current_preference_name):
        res_num = res_num + 1
        print('{} and {} are already matched! \n'.format(current_preference_name.capitalize(),
                                                         hospitals[hos_num].get_name().capitalize()))
    # Check if the current potential hospital has a smaller index than the hospital Resident is currently matched to
    elif (residents[current_preference_index].preferences.index(residents[current_preference_index].current_match) >
          residents[current_preference_index].preferences.index(hospitals[hos_num].name)):
        # Break them up. Remove matching  |  Remove resident's current match  |  add new current match  |  add new
        # match
        print(
            "{} rejects {} and decides to go with {} \n".format(residents[current_preference_index].name.capitalize(),
                                                                residents[current_preference_index].current_match.
                                                                capitalize(),
                                                                hospitals[hos_num].name.capitalize()))
        for i in range(len(matching) - 1, -1, -1):
            if (matching[i][0].get_name() == residents[current_preference_index].current_match and
                    matching[i][1] == residents[current_preference_index].name):
                del matching[i]
                break
        # Move rejected hospital to end of list
        old_match_index = None
        for h in range(len(hospitals) - 1, -1, -1):
            if hospitals[h].name == residents[current_preference_index].current_match:
                old_match_index = h
        old_hospital = hospitals[old_match_index]
        del hospitals[old_match_index]
        hospitals.append(old_hospital)
        hos_num = hos_num - 1
        # Reformat the resident, hospital, and matching information
        residents[current_preference_index].current_match = hospitals[hos_num].name
        hospitals[hos_num].currently_matched.append(current_preference_name)
        matching.append((hospitals[hos_num], residents[current_preference_index].name))
        # Check whether to move on to next hospital
        if len(hospitals[hos_num].currently_matched) >= int(hospitals[hos_num].get_slots()):
            hos_num += 1
            if not hos_num >= len(hospitals):
                cur_hospital = hospitals[hos_num]
            res_num = 0
    else:
        print("{} is happy with {} and rejects {} \n".format(current_preference_name.capitalize(),
                                                             residents[
                                                                 current_preference_index].current_match.capitalize(),
                                                             hospitals[hos_num].name.capitalize()))
        res_num += 1

print("")

print_matching = []

# Place hospital matches together based on hospital name
for hospital in hospitals:
    for i in range(len(matching) - 1, -1, -1):
        if matching[i][0].name == hospital.name:
            print_matching.insert(0, matching[i])

print("Pre-format Matching:\n")
for (hospital, resident) in matching:
    print(hospital.name, resident)

print("\n\nRe-formatted Matching: \n")
for (hospital, resident) in print_matching:
    print("{}: {}".format(hospital.name.capitalize(), resident.capitalize()))


def format_residents(current_hospital):
    out_str = ""
    for out_resident in range(len(current_hospital.currently_matched)):
        if out_resident == len(current_hospital.currently_matched) - 1:
            out_str += "{}\n".format(current_hospital.currently_matched[out_resident]).capitalize()
        else:
            out_str += "{}, ".format(current_hospital.currently_matched[out_resident]).capitalize()
    return out_str


print("\n\nOfficial Matching:\n")
official_matching = ""
for hospital in hospitals:
    official_matching += "{}, {}".format(hospital.name.capitalize(), format_residents(hospital))
print(official_matching)

# Create new CSV file and write official matching to it
lines = official_matching.split("\n")
file_out = "output.csv"
with open(file_out, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for line in lines:
        values = line.split(',')
        csv_writer.writerow(values)

print(f"\nOfficial Matching has been written to {file_out}")