import csv
import sys


# Custom sorting function to sort buildings by their right x-coordinate
def sort_buildings(sortedBuilding):
    return sortedBuilding[1]


# Function to get the outer shape of the skyline
def get_outer_shape(buildingInput):
    shapedSkyline = []
    currentBuildings = []

    for currentBuilding in buildingInput:
        height, left, right = currentBuilding
        # Add the left and right bounds of the current building to the skyline
        currentBuildings.append((left, right, height))
        # Sort the buildings by the right x-coordinate
        currentBuildings.sort(key=sort_buildings)

        # End any buildings that should have ended inside this building
        i = 0
        while i < len(currentBuildings):
            if currentBuildings[i][1] <= left:
                currentBuildings.pop(i)
            else:
                break

        # Get the height of the current skyline
        max_height = currentBuildings[-1][2] if currentBuildings else 0

        # Adjust height of current skyline
        if not shapedSkyline or shapedSkyline[-1][0] != max_height:
            shapedSkyline.append((max_height, left))

    return shapedSkyline


# Create the file reader to read skyline array. input from [filename].csv
def get_input(fileName):
    buildingArray = []
    with open(f'InputsOutputs/{fileName}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            building = tuple(map(int, row))
            buildingArray.append(building)  # Record each building as a tuple

    return buildingArray


# Create the file writer to output skyline array. Output to [filename].csv
def set_output(fileName):
    with open(f"InputsOutputs/{fileName}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in skyline:
            writer.writerow(row)


buildings = get_input("input1")
# Call function to find skyline shape
skyline = get_outer_shape(buildings)
print(skyline)
set_output("output1")

buildings = get_input("input2")
# Call function to find skyline shape
skyline = get_outer_shape(buildings)
print(skyline)
set_output("output2")

buildings = get_input("input3")
# Call function to find skyline shape
skyline = get_outer_shape(buildings)
print(skyline)
set_output("output3")

buildings = get_input("input4")
# Call function to find skyline shape
skyline = get_outer_shape(buildings)
print(skyline)
set_output("output4")

buildings = get_input("input5")
# Call function to find skyline shape
skyline = get_outer_shape(buildings)
print(skyline)
set_output("output5")
