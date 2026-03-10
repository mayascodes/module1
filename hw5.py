"""
Write a program that will "merge" the two dictionaries (d1 and d2)."""
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}


d1.update(d2)
print(d1)
print(d2)

"""Write a program to Match key values in two dictionaries
Sample Output""" 
A = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Science' : 97, 'Social' : 89}
B = {'Tamil' : 78, 'English' : 68, 'Maths' : 88, 'Science' : 97, 'Social' : 56}


for key in A:
    if key in B and A[key] == B[key]:
        print(key, "=", A[key], "is present in both dictionaries ")



A = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Science' : 97, 'Social' : 89}

dict_items = list(A.items())
print(dict_items)
count = len(A)
for i in range(count):
    for k in range(i + 1, count):
        if dict_items[i][1] > dict_items[k][1]:
            temp = dict_items[i]
            dict_items[i] = dict_items[k]
            dict_items[k] = temp

print(dict_items)
print(f"Before sorting {A}")

sortedA = dict(dict_items)
print(sortedA)




