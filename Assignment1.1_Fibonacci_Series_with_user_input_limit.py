
# Write a Python program to get the Fibonacci series between 0 to user input limit
# Output starts from 0

print()
limit = int(input("limit : "))
print("Fibonacci series : ", end=" ")
num1 = 0
print(num1,end = " ")
num2 = 1
print(num2,end = " ")
next_num = num2
count = 1
while next_num <= limit:
	print(next_num, end=" ")
	count += 1
	num1 = num2
	num2 = next_num
	next_num = num1 + num2
print("\n")