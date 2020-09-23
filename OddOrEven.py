'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
'''

num = int(input("Enter a number: "))
mod = num % 2

if mod > 0:
    print(num, "is an odd number")
else:
    print(num, "is an even number")