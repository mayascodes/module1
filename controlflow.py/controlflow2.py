"""
1.
Write a complete Python that performs the following actions:
Accept a single input from the user and convert it to an integer
If the number is even, display “That is an even number”. If it is odd, display “That is an odd number”.
If the number is negative, display “That is a negative number”. If it is zero or positive, display “That is a positive number”.

2. Write a program that calculates the price of an airline ticket based on destination distance and age of the passenger:
Distance less than 1000 miles:
Children (age < 12): $200
Adults (age 12-64): $300
Seniors (age >= 65): $250
Distance 1000 miles or more:
Children: $400
Adults: $500
Seniors: $450
"""
"""
age = int(input("What is your age: "))
distance = int(input("What is your destination distance: "))

if age < 12:
    if distance >= 1000:
        price = 200 + 400
    else:
        price = 200 
elif age >= 12 and age <= 64:
    if distance >= 1000:
        price = 300 + 500
    else:
        price = 300
elif age >= 65:
    if distance >= 1000:
        price = 250 + 450
    else:
        price = 250

print(f"Your price is:{price}")



2. Create a program that calculates income tax based on income and deductions:
Income tax rates:
0% for income up to $10,000
10% for income between $10,001 and $50,000
20% for income above $50,000
Deductions:
5% deduction if health insurance is paid
10% deduction if charitable donations are made
"""

income = int(input("Enter your income: "))
if income <= 10000:
    tax = 0
elif income > 10000 and income <= 50000:
    tax = income * 0.1
else:
    tax = income * 0.2

deduction = 0

paid = input("Is health insurance paid YES/ NO: ")
if paid == "YES":
    deduction += 0.05


donations = input("Have you made charitable donation YES/NO: ")
if donations == "YES":
    deduction += 0.1

print(tax - (tax * deduction))



