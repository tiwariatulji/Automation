for i in range(1,6):
    print(i)

i = 1       # while loop working untill condition is true'''
while (i <51 ):
    print(i)
    i = i + 1

i = 0       # for loop working untill condition is true
for i in range(0, 51):
    print(i)

i = 0 
while (i <5):
    print("Atul Tiwari")  
    i = i + 1  

i = 0
for i in range(0, 5):
    print("Atul Tiwari")  
    i = i + 1

atul = [1,"Atul",False,1.2,"Subhanmandi"]    
i = 0
while(i<len(atul)):
    print(atul[i])
    i = i + 1

atul_2 = [1,"Atul",False,1.2,"Subhanmandi"]
for i in atul_2:
    print(i)

l = [1,2,3,4,5,6,7,8,9,10]
for i in l  :
  print(i)    


l2 = (1,2,3,4,10)
for i in l2  :
    print(i)  

s = "Hello World"
for i in s  :
    print(i)    






name = [1,2,3]
for i in name:
    print(i)
else:
    print("End of the loop")    
# ---------------- Break statement-----------------// this is used to break the loop
name = [1,2,3]
for i in name:
    print(i)
    if i == 2:
        break
    
else:
    print("End of the loop")


# ---------------- Continue statement----------------- // this is used to skip the loop
name = [1,2,3]
for i in name:
    if i == 2:  
        continue
    print(i)
else:   
    print("End of the loop")

# ------------Pass statement----------------- // this is used to skip the loop
name = [1,2,3]
for i in name:  
    pass
    print(i)    


for i in range(100):
    if(i==32):
        break
    print(i)

for i in range(100):
    if(i==32):
        continue
    print(i)

    #  ------- Exercise ---------
    # 1. Write a program to print multiplication table of a given number using for loop.
    n= int(input("Enter the number:"))

    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

# 2.   Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]     # 

# name = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in