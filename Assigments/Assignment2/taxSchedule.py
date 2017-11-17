# Student Name: Edward Ma
# Student ID: W0057568
# Date: October 17, 2016
# Assignment 2 Program 3


# function for total tax, base on tax table of if user is single or married
def totalTax(x,y):
    #if user enter single, it will run the follow if function and return tax base on their income
    if x.lower() == "single":
        if y > 0 and y <= 8000:
            return y * .10
        elif y > 8000 and  y <= 32000:
            return 800 + ((y - 8000) * .15)
        else:
            return 4400 + ((y - 32000) * .25)
    #if user enter married, it will run the follow if function and return tax base on their income
    elif x.lower() == "married":
        if y > 0 and y <= 16000:
            return y * .1
        elif y > 16000 and y <= 64000:
            return 1600 + ((y-16000)*.15)
        else:
            return 8800 + ((y-64000)*.25)
    else:
        print("Invalid Input! Try Again")
        exit()

# user input global value
maritalStatus = input("Enter your marital status: ")
taxableIncome = float(input("Enter your taxable income: "))

# output display result to user.
print("Your total tax is ${:.2f}".format(totalTax(maritalStatus, taxableIncome)))