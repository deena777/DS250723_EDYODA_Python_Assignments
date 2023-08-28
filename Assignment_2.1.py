'''
Fun with Lists and Tuples

Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a 
given list of non-empty tuples.

'''

num_tuples = int(input("\nEnter the number of tuples: "))
tuple_list = []
for i in range(num_tuples):
    tuple_input = input(f"Enter elements for tuple {i+1} (comma-separated): ")
    elements = tuple_input.split(',')
    tuple_elements = tuple(map(int, elements))
    tuple_list.append(tuple_elements)
print("User input list of tuples:", tuple_list)
n = len(tuple_list)
for i in range(n):
    for j in range(0, n-i-1):
        if tuple_list[j][-1] > tuple_list[j+1][-1]:
            tuple_list[j], tuple_list[j+1] = tuple_list[j+1], tuple_list[j]
print("Rearranged list of tuples:", tuple_list)
