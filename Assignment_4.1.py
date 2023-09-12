'''
# Play with Lambda

# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

sample input: 10
sample output: 35

'''

add = lambda x : x + 25

number = int(input("Enter the number : "))
result = add(number)

print(f"{number} + 25 = {result}")