#Create a program with a for loop and a break statement. 
# The program should iterate over characters in an email 
# address, exit the loop when it
# reaches the @ symbol, and print the part before @ on one line
name = ""
email = input("enter your email: ")

for letter in email :
    if letter == '@':
        break
    else:
        name = name + letter

print(name)