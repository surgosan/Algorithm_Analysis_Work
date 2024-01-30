import Hospital
import Resident

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

h1.print_preferences()
h1.print_slots()
print(h1.get_preferences())