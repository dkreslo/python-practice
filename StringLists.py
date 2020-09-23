'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

string = input("Please enter a word to check for a palindrome: ")
new = []

for i in string:
    if i == string[-1]:
        new.append(i)

print(new)