import csv


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


# Read buildings from CSV
buildings = []
with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        building = tuple(map(int, row))
        buildings.append(building)  # Record each building as a tuple

# Call function to find skyline shape
skyline = get_outer_shape(buildings)
print(skyline)

# Create the file writer to output skyline array. Output to output.csv
