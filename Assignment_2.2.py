'''
Make Your Own mini-Dictionary

Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be 
corresponding ASCII values

'''
# From a-z

ascii_dict = {}
for letter in range(ord('a'), ord('z') + 1):
    ascii_dict[chr(letter)] = letter
for key, value in ascii_dict.items():
    print(f"{key}: {value}")
