import csv
CR = ['CR', 'CR', 'CR']  # datalist[0][3:6] Crusier coordinates
CRHitList = []

fileName = "map.txt"  # file to read
accessMode = "r"  # access permission
INPUT = open(fileName, accessMode)
# Read the file contents
dataPlaceholder = csv.reader(INPUT)
datalist = []  # a list with each line as value
for row in dataPlaceholder:
    datalist.append(row)

fileName1 = "battlemap.txt"  # file to read
accessMode1 = "r"  # access permission
with open(fileName1, accessMode1) as INPUT1:
    # Read the file contents
    dataPlaceholder1 = csv.reader(INPUT1)
    datalist1 = []  # a list with each line as value
    for row in dataPlaceholder1:
        datalist1.append(row)

for i in datalist1:
    print(' '.join(i))

guess_y = int(input("Y Coord "))
guess_x = int(input("X Coord "))
if datalist[guess_y][guess_x] == '0':
    datalist1[guess_y+1][guess_x+1] = '0'
    for i in datalist1:
        print(' '.join(i))
    print("You Missed!")
else:
    print(datalist[guess_y][guess_x], "It's a hit! OUCH!")
    if datalist[guess_y][guess_x] == 'CR':
        CRHitList.append(datalist[guess_y][guess_x])
        datalist1[guess_y+1][guess_x+1] = 'X'
        if CR == CRHitList:
                print("You sunk a Cruiser!")
    for i in datalist1:
        print(' '.join(i))




