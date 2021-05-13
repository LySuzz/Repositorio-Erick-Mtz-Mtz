import csv
list = [["RN", "Name", "GRADES"],
    [1, 'ABC', 'A'],
    [2, 'TUV', 'B'],
    [3, 'XYZ', 'C']]
with open('studentgrades.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
    writer.writerows(list)