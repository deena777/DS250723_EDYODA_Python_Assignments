'''
Make Your Own mini-Dictionary

Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be 
corresponding ASCII values - for user input range of alphabets


'''

ascii_dict = {}
startchar = input("Starting alphabet: ")
endchar = input("ending alphabet: ")
for letter in range(ord(startchar), ord(endchar) + 1):
    ascii_dict[chr(letter)] = letter
print(ascii_dict)