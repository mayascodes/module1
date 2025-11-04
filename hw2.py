num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    result = num1 - num2
elif num1 < num2:
    result = num1 + num2
else:
    result = num1 * num2

print (result)

#

divisby400 = False
leap = False

year = int(input("Enter a year: "))
remainder = year % 400

if remainder == 0: 
    divisby400 = True
else:
    rem = year % 4
    rem2 = year % 100
    if rem == 0 and rem2 != 0:
        leap = True

if leap == True or divisby400 == True:
    print("This is a leap year")
else:
    print("This is not a leap year")

###
if year % 400 == 0:
    print("This is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("This is a leap year")
else:
    print("This is not a leap year")

###
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("This is a leap year")
else:
    print("This is not a leap year")