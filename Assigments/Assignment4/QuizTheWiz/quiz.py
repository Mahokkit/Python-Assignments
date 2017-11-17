"""
Student Name: Edward Ma
Student ID: W0057568
Date: November 16, 2016

Quiz the Wiz
Develop a quiz program that will load multiple-choice questions and answers from a text file.
The program will then display each question and ask the user for their guess. Once the questions have been asked,
total the correct answers and display the user’s grade.
"""
import math
import csv
fileName = "quiz.txt" #file to read
accessMode = "r" #access permission
score = 0

with open(fileName, accessMode) as INPUT:
    #Read the file contents
    dataPlaceholder = csv.reader(INPUT)
    datalist = [] #a list with each line as value
    for row in dataPlaceholder:
        datalist.append(row)
counter = 0
for question in range(len(datalist)):
    #loop for the lenght of the list, it will loop to each value within the list that is the list
    #last values of each list item is the correct answer
    print("Question {}\n".format(question+1))
    print("Fill in the blank\n"+str(datalist[question][0]),"\nA)"+str(datalist[question][1])+"\nB)"
          +str(datalist[question][2])+"\nC)"+str(datalist[question][3])+"\nD)"+str(datalist[question][4])+"\n")
    answer = input("What is the correct answer? ")
    if answer.upper() == datalist[question][5]: #check to see if user input is the correct answer.
        score += 1 #if it's correct, it will add the score.
    print()

finalScore = (score/len(datalist))*100 #calculate final score
print("You Final Score is: {0}/{1} or {2:.2f}%".format(score, len(datalist), finalScore)) #show the user how well they did