#Author: Edward Ma
#Student ID: W0057568
#Date: 09-26-2016

#Imperial To Metric Conversion
#using the formula
#inch = 63360 * miles + 36 * yards + 12 * feet + inch
#metres = total inch / 39.37
#kilometres = int(metres/1000)
#int() to ensure all input data is converted to a integers
miles = int(input("Please Enter Numbers of Miles: "))
yards = int(input("Please Enter Numbers of Yards: "))
feet = int(input("Please Enter Numbers of Feet: "))
inches = int(input("Please Enter Numbers of Inches: "))

#convert set of data to total inches
totalInches = (63360*miles)+(36*yards)+(12*feet)+inches
#convert inches to metres
metres = totalInches/39.37
#convert metres to kilometres, there's 1000metres in 1 kilometres
kilometres = int(metres/1000)
#convert metres to centimetres, there's 100 centimetres in 1 metres
centimetres = metres*100

# Metres%1000 will show the amount that is left over after taking as many set of "1000"
print("The Metric Length is", kilometres,"kilometres,",
      int(metres%1000), "metres and",
      round(centimetres%100,1), "centimetres")

