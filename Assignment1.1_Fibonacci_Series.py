
# Write a Python program to get the Fibonacci series between 0 to 50
# With expected output : 1 1 2 3 5 8 13 21 34

print()
print("Fibonacci series : ", end=" ")
num1 = 0
num2 = 1
print(num2,end = " ")
next_num = num2
count = 1
while next_num <= 50:
	print(next_num, end=" ")
	count += 1
	num1 = num2
	num2 = next_num
	next_num = num1 + num2
print("\n")
