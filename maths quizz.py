import random
import numbers
import time

title = "** A Simple Math Quiz **"
print(title)

while True: #the first question
    print("quesion 1")
    question1 = str(input("what is 5 + 5:  "))

    if question1 == "10":
        print("well done, you are correct")
        break

    if question1 != "10":
        print("please try again")

while True: #the second question
    print("question 2")
    question2 = str(input("what is 5 to the power 2:  "))

    if question2 == "25":
        print("well done, lets move onto the next to question")
        break

    if question2 != "25":
        print("try again!")

while True:
    print("question 3")
    question3 = str(input("what is the value of ℼ"))

    if question3 == "3.14":
        print("correct")
        break

    if question3 != "3.14":
        print("unlucky try again!")

while True:
    print("question 4")
    question4 = input("which is the correct way to work out the area of a circle?:  ")
    print("option A = ℼ x radius + radius")
    print("option B = ℼ x (radius x radius)")

    if question4 == "option A" or "option a":
        print("incorrect, try again!")

    if question4 == "option B" or "option b":
        print("CORRECT!!!!!")
        break

while True:
    print("question 5")
    question5 = str(input("what is the square root of 64:   "))

    if question5 == "8":
        print("genius?")
        break

    if question5 != "8":
        print("cmon, this was an easy one😂")

while True:
    print("question 6")
    question6 = str(input("what is 9 the power of 3:   "))

    if question6 == "729":
        print("wow, if you worked that out in your head then your a genius")
        break

    if question6 != "729":
        print("keep thinking")

# while True:
#     print("question 7")
#     question7 = str