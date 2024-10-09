#  List is container to store set of values of any data type
#  List is mutable
#  List is ordered
#  List is indexed
#  List is allow duplicate values
#  List is dynamic

friends = ["Atul","Orange","Rohit","Akash","5","240.6"]
print(friends)
print(type(friends))

friends1 = ["Atul","Orange",5,240.6,"Akash","Rohit"]
friends1 [1] = 'Mango'
print(friends1)

print(friends1[3])
# List indexing
print(friends1[0:3])
print(friends1[1:4])

# List Methods 
friends2 = ["Atul","Orange",5,240.6,"Akash","Rohit"]

friends2 .append("Mango")

# shrot method
l1 = [5,6,3,2,1]
l1.sort()
print(l1)

# reverse method
l1.reverse() 
print(l1)

# append method
l1.append(7)
print(l1)

# insert method
l1.insert(2,8)
print(l1)

# pop method 
l1.pop(2)
print(l1)

# remove method
l1.remove(5)
print(l1)

# ---------------------------------

Marks = []

f1 = int(input("Enter Marks 1 : "))
Marks.append(f1)
f2 = int(input("Enter Marks 2 : "))
Marks.append(f2)
f3 = int(input("Enter Marks 3 : "))
Marks.append(f3)

Marks.sort()
Marks.remove(20)
# Marks.pop(2)


print(Marks)

# -----------------------
l = [1,2,3,4,5,6,7,8,9,10]

print(sum(l))
