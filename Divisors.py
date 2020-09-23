'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''

num = int(input("Enter a number: ")) #number get
listRange = list(range(1, num + 1))  #creates the range of the list

divisorList = []

for number in listRange:
    if num % number == 0: #checks for no remainder, meaning it is a divisor
        divisorList.append(number) #adds number to list if ot is

print(divisorList)

