
# tuple is a collection of elements enclosed within () and immutable
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, "Hello", True, 3.14)
tup3 = tuple([1, 2, 3, 4, 5])  # creating a tuple from a list

print(tup1)
print(tup2)
print(tup3)

print(tup1[0])  # accessing elements using indexing
print(tup2[1:4])

print(len(tup1))  # getting the length of a tuple
print(len(tup2))

print(tup1 + tup2)  # concatenating two tuples
print(tup1 * 3)  # repeating a tuple

print(3 in tup1)  # checking if an element is present in a tuple
print(6 in tup1)

for x in tup2:  # iterating over a tuple
    print(x)

print(max(tup1))  # getting the maximum element in a tuple
print(min(tup1))  # getting the minimum element in a tuple

# converting a tuple to a list
list1 = list(tup1)
print(list1)

# converting a list to a tuple
tup4 = tuple(list1)
print(tup4)

# --------------------------

a = (1, 2, 3)
print(type(a))
no = a.count(1)
print(no)

b = (1,2,3,False,"Rohit","Shivam")
print(b)
print(type(b))


d = (1,2,3,3,4,5,6)

e = d.count(1)
print(e)