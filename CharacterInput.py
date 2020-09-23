'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
year = 2018

if age <= 0:
    print("Not born yet!")
elif age > 0 and age < 100:
    year = str((year - age) + 100)
    print(name, "will be 100 years old in", year)
elif age == 100:
    print(name, "is 100 years old!")
elif age > 100:
    print(name, "is over 100 years old!")