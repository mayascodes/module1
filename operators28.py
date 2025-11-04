"""
#1. Write a program to take two numbers as user input and perform the following task–
a. If the first number is bigger than the second number, perform subtraction.
b. If the first number is smaller than the second number, perform addition.
c. If the two numbers are equal, perform multiplication.
"""
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a 2nd number: "))

if num1 > num2:
    ans = num1 - num2
elif num1 < num2:
    ans = num1 + num2
else:
    ans = num1 * num2
print(ans)

"""
"""
Write a program to take two two numbers and as an user input and perform the following task -
Use Ternary Operator to find smaller number among two and print it.
Bitwise AND
Bitwise OR
Bitwise NOT for first number
1 bit LEFT and 2 bit RIGHT shift of second number
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    bigger = num1
else:
    bigger = num2
print(bigger)

#ternary operator
bigger = num1 if num1 > num2 else num2

#bitwise AND
print(num1 & num2)

#bitwise OR
print(num1 | num2)

#bitwise NOT 
print
