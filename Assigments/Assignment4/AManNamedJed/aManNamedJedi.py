"""
Student Name: Edward Ma
Student ID: W0057568
Date: November 16, 2016

A Man Named Jedi
Create a program that will read in a file and add line numbers to the beginning of each line.
Along with the line numbers, the program will also pick a random line in the file and convert it to all capital letters.
All other lines in the program will be converted to lowercase letters. The program will then write the resulting lines
out to a second file and display the contents of each file on the console.
"""
import csv #use cool csv function bruh
import random #to allow random number to be made! wooooooah!

fileName = "AManNamedJed.txt"
fileName2 = "AManNamedJed2.txt" #second file name
accessMode = "r" #to read the file
accessMode2 = "w" #to write the file

print("***ORIGINAL TEXT***\n")
with open(fileName, accessMode) as INPUT:
    #Read the file contents
    dataPlaceholder = csv.reader(INPUT)
    datalist = [] #a list with each line as value
    counter = 0
    data = []
    for row in dataPlaceholder:
        counter += 1 #add line number to the list!
        print(' '.join(row))
        data = str(counter)+": "+str(' '.join(row))
        datalist.append(data)

randomLine = random.randint(0,(len(datalist))) #set random number to go as far as length of the list

print("\n***NEW TEXT***\n")
with open(fileName2, accessMode2) as OUTPUT:
    for counter in range(len(datalist)):
        if counter == randomLine:
            #IF the row is samn as random number, change it to uppercase
            #If not, make it lowercase
            OUTPUT.write(datalist[randomLine].upper()+str("\n"))
        else:
            OUTPUT.write(datalist[counter].lower()+str("\n"))

with open(fileName2, accessMode) as SHOW: #Read new file, and print out what happened!
    #Read the file contents
    dataPlaceholder = csv.reader(SHOW)
    datalist1 = [] #a list with each line as value
    for row in dataPlaceholder:
        datalist1.append(row)

for row in datalist1:
    print(' '.join(row))