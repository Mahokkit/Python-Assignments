# Student Name: Edward Ma
# Student ID: W0057568
# Date: October 17, 2016
# Assignment 2 Program 2

# Detail of Requirement:
# user input water usage in cubic feet
# program output total charge
# if usage is 1000 or below, charge $15
# if usage is over 1000 up to and equal to 2000,  $0.0175 per cubic feet
# ex: 2000 * 0.0175
# if usage is over 2000 up to and equal to 3000,  $0.02 per cubic feet
# ex: 3000 * 0.02
# if usage is over 3000, flat rate is $70

# user input value of water usage
waterUsage = float(input("Enter usage of water (cubic feet): "))

# function that calculate total charge of usage, base on detail of requirement
def totalCharge(x):
    if x > 0 and x <=1000:
        return 15
    elif x > 1000 and x <= 2000:
        return x*0.0175
    elif x > 2000 and x <= 3000:
        return x*0.02
    else:
        return 70

# output total charge to user
print("Total Charge is ${0}".format(totalCharge(waterUsage)))