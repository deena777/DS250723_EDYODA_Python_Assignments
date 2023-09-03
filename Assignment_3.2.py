'''
String inside the function

Write a Python program to reverse a string.

Sample String : "1234abcd"
Expected Output : "dcba4321"

'''

def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter a string: ")

reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)