list1 = []
print(list1)

tuple1 = ()
print(tuple1)

list2 = [1,5,4,6,5,3]
list3 = list2[7:10]
print(list3)

print(list2[7:10])

tuple2 = (1,3,2,3,4,2)

tuple3 = tuple2[7:10]
print(tuple3)

print(tuple2[7:10])

# print(list2[7]) 
# print(tuple2[7])

tuple4 = 1,2,3,4,3,5
print(tuple4)

if 6 in tuple4:
    print("true")
else:
    print(False)

if 10 not in tuple4:
    print(True)
else:
    print(False)

tuple5 = tuple2 + tuple4
print(tuple5)

tuple6 = tuple5 * 2
print(tuple6)

list4 = [1,6,4,3,7,5]
list5 = list4 + list2
print(list5)

list6 = list5 * 2
print(list6)

name = "python"
newname = "".join(reversed(name)) # "".join joins the letters together with nothing separating them, reversed function reverses the order of the items
print(newname)