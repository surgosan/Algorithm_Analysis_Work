import csv


def get_input(fileName):
    with open(f'InputsOutputs/{fileName}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

