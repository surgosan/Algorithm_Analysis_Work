import csv

# Read the input csv and put tuples into the buildings list
buildings = []
with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        building = (int(row[0]), int(row[1]), int(row[2]))
        buildings.append(building)

