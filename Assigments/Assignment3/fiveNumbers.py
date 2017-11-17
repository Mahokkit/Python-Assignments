# Student Name: Edward Ma
# Student ID: W0057568
# Date: October 26, 2016
# Assignment 3 Program 1

listOfValues = []
maxLengthList = 5
count = 0
while len(listOfValues) < maxLengthList:
    count += 1
    values = input("Enter value #{0}: ".format(count))
    listOfValues.append(values)

print("This is your list")
print(' '.join(listOfValues))

listOfValues.reverse()
print("\nThis your list reversed! VIOLA!")
print(', '.join(listOfValues))

listOfValues = list(map(int, listOfValues)) #convert string to list

print("\nThe average of the number is:", sum(listOfValues)/len(listOfValues))

print("\nNumber that are greater than the average: ")
for i in listOfValues:
    if i > (sum(listOfValues)/len(listOfValues)):
        print(i)