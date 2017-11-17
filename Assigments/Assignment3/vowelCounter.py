"""
Student Name: Edward Ma
Student ID: W0057568
Date: October 27, 2016
Assignment 3 Program 2
"""
while True:
    userInputPhase = input("Enter a Sentence/Phase or 'Quit' to exit the program: ")
    if userInputPhase.lower() == "quit":
        print("You have enter '{}', Good bye!".format(userInputPhase))
        exit()
    else:
        userInputPhase = userInputPhase.lower()
        print("\nYou have enter: " ,userInputPhase)
        print("Here are your vowel counts!")
        print("Letter A count: " ,userInputPhase.count("a"))
        print("Letter E count: " ,userInputPhase.count("e"))
        print("Letter I count: " ,userInputPhase.count("i"))
        print("Letter O count: " ,userInputPhase.count("o"))
        print("Letter U count: " ,userInputPhase.count("u"))
        print()