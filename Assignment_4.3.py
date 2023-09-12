'''
# Find the Squares from the given List

# Write a Python program to square the elements of a list using map() function.

Sample List: [4, 5, 2, 9]
Square the elements of the list: [16, 25, 4, 81]
'''

# input from user
size = (int(input("Enter the length of the list: ")))
lst = []
for i in range (size):
    ele = int(input("Enter the elements:"))
    lst.append(ele)
print("list : ",lst)

# square the list
square = lambda x : x**2
square_list = list(map(square,lst))
print("Square the elements of the list: ",square_list)
