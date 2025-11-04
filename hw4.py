num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

larger = num1 if num1 > num2 else num2

print(f"The larger number is: {larger}")

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

if (num1 % 2 == 0) and (num2 % 2 == 0):

    print("Both numbers are even")
else:

    print("Both numbers are not even")

if num1 == num2:

    print("Both numbers are equal")
else:

    print("The numbers are not equal")

num1, num2 = num2, num1

print( f"num1 = {num1}, num2 = {num2}")