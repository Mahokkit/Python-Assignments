#Author: Edward Ma
#Student ID: W0057568
#Date: 09-26-2016

#Car Loan Calculator that calculate monthly payment
#using formula
#monthly payment = (i / 1 - (1+i)^-12n)*A
#i = r / 1200
#n = years
#A = amount borrowed at r% interest

print("Welcome To Monthly Car Loan Calculator")
print()
#using float() to allow decimal in calculation
amountBorrowed = float(input("Please Enter Amount Borrowed: "))
interestRate = float(input("Please Enter Interest Rate (%): "))
#int() so input data is converted to a integers
numberOfYear = int(input("Please Enter The Number of Years: "))

i = interestRate/1200
# ** for exponent ex 2^2 is 2**2
monthlyPayment = (i/(1-(1+i)**(-12*numberOfYear)))*amountBorrowed
print()
#{:2.f} as 'placeholder' for monthlyPayment,
# output - "Your Monthly Payment is $xxx.xx." .2f round to 2 decimal places.
print("Your Monthly Payment is ${:.2f}".format(monthlyPayment))
