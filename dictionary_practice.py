students = {'Name': 'Maya', 'Age': 17, 'Bday': 102009}


#modifying a dictionary
students['Age'] = 15

#adding a new key and value pair
students['Grade'] = 12

#inserting an item
students.update({'Score': 75})
students.update({'Age': 17})

print(students)


#will only print keys
for item in students:
    print(item)

#printing each key and value pair
for k, v in students.items():
    print("key is: ",k, "value is: ",v)

#OR
print('**************************')
for k in students:
    print(k,students[k])

#only printing values
for v in students.values():
    print("Here are the values:", v)


#removing a key
del students['Score']
print(students)

#deleting the last item
print(students.popitem())

#del students['Score'] KeyError: not in dictionary
#print(students)

#printing the number of items in a dictionary
number= len(students)
print(number)

#checking if a key exists
if 'Name' in students:
    print("The key exists")
else:
    print("The key does not exist")


if 'Score' in students:
    print("The key exists")
else:
    print("The key does not exist")


student2 = students.copy()

students.clear()
print(students)

print(student2)

ageValue = student2.get('Age')
print(ageValue)


