# Student Name: Edward Ma
# Student ID: W0057568
# Date: October 16, 2016
# Assignment 2 Program 1

# detail of requirement:
# Compute price of desk base on the following detail
# charge for desk is $200 min
# if surface is over 750 inch^2 add $50
# if mahogany add $150, if oak add $125, no charge for pine
# $30 per drawer in the desk
# user input order number, desk length & width, wood type, and number of drawer
# program output the price.

# declare global variable
minChargeOfDesk = 200
costOfSurfaceArea = 0
costOfWood = 0
costOfDrawer = 0

# user input value per variable
orderNumber = input("Enter Order Number: ")
deskLength = float(input("Enter Length of Desk (inches) : "))
deskWidth = float(input("Enter Width of Desk (inches): "))
typeOfWood = input("Enter Type of Wood (Mahogany, Oak, or Pine): ")

# if-else function for type of wood, and end if it's not one of the 3 options.
if typeOfWood.lower() == "mahogany":
    costOfWood = 150
elif typeOfWood.lower() == "oak":
    costOfWood = 125
elif typeOfWood.lower() == "pine":
    costOfWood = 0
else:
    print("Error. Incorrect Response. Please Try Again!")
    exit()

# user input value of variable contiune!
numberOfDrawer = int(input("Please Enter Number of Drawer: "))

surfaceArea = deskLength * deskWidth

# if-else function for surface area, and declare value base on user input
if surfaceArea > 750:
    costOfSurfaceArea = minChargeOfDesk + 50
else:
    costOfSurfaceArea = minChargeOfDesk
# calculating value of variable
costOfDrawer = numberOfDrawer * 30

totalPrice = costOfSurfaceArea + costOfWood + costOfDrawer

# output and display to user
print("Total Cost is: ${:.2f}".format(totalPrice))
