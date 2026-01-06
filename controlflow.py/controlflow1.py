"""
1. Write a complete Python that performs the following actions:
Accept a single input from the user and convert it to an integer
If the number is even, display “That is an even number”. If it is odd, display “That is an odd number”.
If the number is negative, display “That is a negative number”. If it is zero or positive, display “That is a positive number”.
"""

num = input("Enter a number: ")
num = int(num)

print("That is an even number") if num%2 == 0 else print("That is an odd number")


print("That is a negative number") if num < 0 else print("That is a positive number")

"""
Write a program that determines the priority of a patient based on their condition and age:
Critical condition (age < 12 or age ≥ 65): Highest priority
Serious condition (age 12–64): Medium priority
Stable condition (age ≥ 18 and < 65): Lowest priority
"""
age = int(input("Enter your age"))

if (age < 12 or age >= 65):
    print("critical condition, highest priority")
    
elif (age> 12 and age<64):
    print("serious condition, medium priority")

else:
    print("stable condition, lowest priority")