name = "maya solanki"
print(name.upper())
print(name.lower())
print(name.title())
print(name.swapcase())

name2 = "AARAV SOLANKI"
print(name2.swapcase())
print(name2.capitalize())
print(name2.count("A"))
print(name2.find("q"))  #if found, gives index number, if not, gives -1
#print(name2.index("p")) #gives error if not found
print(name2.split(" ")) #splits at space, stores split data in a list

names = ["maya", "aarav", "mia", "sarina"]
joinednames = "/".join(names)
print(joinednames)