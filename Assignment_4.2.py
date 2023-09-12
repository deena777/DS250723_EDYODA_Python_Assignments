'''
# Find the way with Maps

# Write a Python program to triple all numbers of a given list of integers. Use Python map.

sample list: [1, 2, 3, 4, 5, 6, 7]
Triple of list numbers: [3, 6, 9, 12, 15, 18, 21]
'''


# input from user
size = (int(input("Enter the length of the list: ")))
lst = []
for i in range (size):
    ele = int(input("Enter the elements:"))
    lst.append(ele)
print("list : ",lst)

# tripling of list
triple = lambda x : x*3
triple_of_lst = list(map(triple,lst))
print("Triple of list numbers : ",triple_of_lst)
