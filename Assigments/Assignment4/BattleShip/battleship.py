"""
Student Name: Edward Ma
Student ID: W0057568
Date: November 16, 2016

Battleship
Each occurrence of the number one in the map indicates a ship location.
The goal of this simplified version of the Battleship game is to sink all ships before running out of missiles.
The goal count down from 30 missiles but you can modify the game to ask how many missiles you’d like to start with
if you wish.
The program should implement all safeguards against user errors such as validating against invalid entries.
"""
import csv #allow CSV reader
import string #import string function!

fileName = "map.txt"  # file to read
accessMode = "r"  # access permission
with open(fileName, accessMode) as INPUT:
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

print("***WELCOME TO THE BATTLESHIP GAME***")
for i in datalist1:
    print(' '.join(i))

x = True
while x:
    try: #error checking, if user enter anything but a digit, it will force them to enter a number, i'm evil
        missiles = int(input("How many missiles do you want? Maximum 30 "))

        x = False
    except ValueError:
        print("Error! You have to enter a number!\n Try again!")

"""
if user try to be a cheeky and try to have more than 30 missiles, this will force it to 30 missiles
nice try cheaters!
"""

if missiles > 30:
    print("Sorry you can't have {} missiles! You have 30 missiles".format(missiles))
    missiles = 30
else:
    print("You have {} missiles".format(missiles))

"""
a bunch of predetermined list of how much hit each class of ship can take
when user successfully hit a target, it will append to the **HitList
coordinate are show next to each respectable list for testing purposes.
"""
totalMissiles = missiles

CR = ['CR', 'CR', 'CR']  # datalist[0][3:6] Crusier coordinates
CRHitList = []
BA = ['BA', 'BA', 'BA', 'BA']  # datalist[1][8], datalist[2][8],datalist[3][8],datalist[4][8] battleship coordinate
BAHitList = []
DE = ['DE', 'DE']  # datalist[4][3], datalist[5][3] destroyer coordinate
DEHitList = []
SU = ['SU', 'SU', 'SU']  # datalist[7][6:9] #submarine coordinate
SUHitList = []
CA = ['CA', 'CA', 'CA', 'CA', 'CA']  # datalist[8][0:5] #carrier coordinate
CAHitList = []

i = 0

while i <= totalMissiles:  # loop will stop once i is over amount of missiles

    x = True
    while x:
        """
        User input XY coordinate, program will split it to a list and if there's more than 3 items, it will
        combine the 2nd and 3rd value together. ex: a10 become ['a', '1', '0']
        so coordinate for y is coord[1]+coord[2] which is 10 and if it doesn't have more than 3 items,
        y coordinate is just coord[1], and if Y is out of range... well the user just wasted a missiles.
        it will also loop back if user enter any alphabet after j
        """
        try:
            XYCoord = input("Please Enter XY Coordinate (Ex: A1): ")
            coord = list(XYCoord)
            x_coord = list(string.ascii_lowercase) #making an alphabet list
            guess_x = coord[0]
            for h in x_coord: #check for location of guess_x in alphabet list, and input the index
                if guess_x == h:
                    guess_x = x_coord.index(h)
            if len(coord) == 1:
                guess_y = coord[0] #if user only enter 1 value, it will show as false on line 104
            elif len(coord) > 2:
                guess_y = coord[1]+coord[2] #if user enter for example A100, it will only show coordinate for Y as 10
            else:
                guess_y = coord[1]

            if guess_y.isdigit():
                guess_x = int(guess_x)+1
                guess_y = int(guess_y)
                x = False
            else:
                print('Error! You have enter an invalid coordinate!\nTry again!')
        except ValueError:
            print("Error! You have to enter a number for Y Coordinate!\n Try again!")

    if guess_x > 10 or guess_y > 10:
        missiles -= 1 #even if user fire out of range like a dumb dumb, they still waste a missile...
        print("What a waste of a missiles!\n"
              "What are you trying hit? CHINA?\n"
              "You have {} Missiles left!\n".format(missiles))
    else:
        """
        a long line of IF statement, if user input hit the anything but 0,
        it will enter in each respectable list and check if its match with a predetermined list
         if it's the same, it will show the user what class of ship they took down.
        """
        missiles -= 1
        if datalist1[guess_y][guess_x] == '0' or datalist1[guess_y][guess_x] == 'X':
            print("You have enter this coordinate before.\nYou have {} Missiles left\n".format(missiles))
        elif datalist[guess_y-1][guess_x-1] == '0':
            datalist1[guess_y][guess_x] = '0'
            for z in datalist1:
                print(' '.join(z)) #show where they hit
            print("You Missed!\nYou have {} Missiles left!\n".format(missiles))
        else:
            datalist1[guess_y][guess_x] = 'X'
            for c in datalist1:
                print(' '.join(c)) #show where they hit
            print("It's a hit! OUCH!\nYou have {} Missiles left!\n".format(missiles))

            if datalist[guess_y-1][guess_x-1] == 'CR':
                CRHitList.append(datalist[guess_y-1][guess_x-1])
                if CR == CRHitList:
                    print("You sunk a Cruiser!\n") #show user what they took out.
            elif datalist[guess_y-1][guess_x-1] == 'BA':
                BAHitList.append(datalist[guess_y-1][guess_x-1])
                if BA == BAHitList:
                     print("You sunk a My BattleShit!\n")
            elif datalist[guess_y-1][guess_x-1] == 'DE':
                DEHitList.append(datalist[guess_y-1][guess_x-1])
                if DE == DEHitList:
                    print("You sunk a Destroyer!\n")
            elif datalist[guess_y-1][guess_x-1] == 'SU':
                SUHitList.append(datalist[guess_y-1][guess_x-1])
                if SU == SUHitList:
                    print("You sunk a Submarine!")
            elif datalist[guess_y-1][guess_x-1] == 'CA':
                CAHitList.append(datalist[guess_y-1][guess_x-1])
                if CA == CAHitList:
                    print("You sunk a Carrier!\n")

    if missiles == 0:  # program automatically end when no missiles left.
        break
    elif CA == CAHitList and CR == CRHitList and SU == SUHitList and BA == BAHitList and DE == DEHitList:
        print("Wow! You hit all the targets! YOU WIN!")
        break
    else: #ask user if they want to keep going...
        decision = input("Want to keep going? Y/N ")
        if decision.lower() == 'n':
            break
        elif decision.lower() == 'no':
            break
        else:
            print("Let's keep going!")
print("Thanks for playing!")