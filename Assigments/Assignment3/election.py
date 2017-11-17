"""
Student: Edward Ma
Student ID: W0057568
Date: October 26, 2016
Assignment 3 Program 3
"""

numberOfCandidate = int(input("Enter the number of Candidate in the election: "))
nameOfCandidate = []
numberOfVote = []
percentOfVote = []
count = 0
while len(nameOfCandidate) < numberOfCandidate:
    count += 1
    values = input("Enter name of Candidate #{0}: ".format(count))
    nameOfCandidate.append(values)
    values = input("Enter the number of votes for Candidate #{}: ".format(count))
    numberOfVote.append(values)

numberOfVote = list(map(int, numberOfVote))

for counter in range(numberOfCandidate):
    percentOfVote.append(round((((numberOfVote[counter])/sum(numberOfVote)) * 100)))

for counter in range(numberOfCandidate):
    if percentOfVote[counter] == max(percentOfVote):
        firstOrLast = "First Place!"
    elif percentOfVote[counter] == min(percentOfVote):
        firstOrLast = "LAST PLACE, WHAT A LOSER!"
    else:
        firstOrLast = ""
    print("{0} - {1}% {2}".format(nameOfCandidate[counter],percentOfVote[counter],firstOrLast))