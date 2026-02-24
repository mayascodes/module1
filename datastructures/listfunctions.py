list1 = [3,6,4,7,8]
list2 = list1

list2[2] = 40
print(list1)

newlist = [m for m in range(1,6)]
print(newlist)

list1.append(12)
print(list1)

list1.insert(3,100)
print(list1)

del list1[3]
print(list1)

print(3 in list1)
print(40 not in list1)

list3 = list1[::2]
print(list3)

newnewlist = []
newlist = newnewlist
print(newlist)

