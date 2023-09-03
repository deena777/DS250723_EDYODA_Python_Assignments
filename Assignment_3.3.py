'''
Calculate the Upper and The lower Case

Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

'''

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

user_input = input("Enter a string: ")

upper, lower = count_upper_lower(user_input)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)