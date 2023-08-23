
# Write a Python program to count the number of even and odd numbers from a series of numbers.
# User input numbers as list

print()
size = (int(input("Enter the length of the list: ")))
lst = []
for i in range (size):
    ele = int(input("Enter the element:"))
    lst.append(ele)

print()
print(lst,"\n")

even_count = 0
odd_count = 0
#print()
for i in lst :
    if i%2 == 0 :
        even_count += 1  
    else: 
        odd_count += 1

print("Number of even numbers :",even_count)      
print("Number of odd numbers :",odd_count,"\n")