#Author: Edward Ma
#Student ID: W0057568
#Date: 09-26-2016

#Work Order Tracking for McNair's PC Repair
#Cost per Hour of Labour is $65.00
#Parts & Supplies  are subject to 15% sale tax (1.15)

print("Welcome to Work Order Tracking for McNair's PC Repair") #welcome message
print()
customerName = input("Please Enter Customer's Name: ")
hourOfLabour = float(input("Please Enter Hours of Labour: ")) #change input value to allow decimal via float()
partAndSupply = float(input("Pleas Enter Cost of Parts & Supplies: "))
print()
costOfLabour = hourOfLabour*65 #calculating total cost of Labour
costOfPartsAndSupplies = partAndSupply*1.15 #Calculating total cost of Parts & Supplies with tax
totalCost = costOfLabour + costOfPartsAndSupplies

print("Work Order Summary for", customerName)
print("Total Labour Cost: ${0:.2f}".format(costOfLabour))
#round output to the near 2 decimal ex: $100.xx
# %s convert variable after % to string.
# So output is - "Total Labour Cost: $99.99", instead of "Total Labour Cost: $ 99.99"
print("Total Parts & Supplies: ${0:.2f}".format(costOfPartsAndSupplies))
print("Total Cost: ${0:.2f}".format(totalCost))



