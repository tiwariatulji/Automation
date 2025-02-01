#-- Function argument 
def goodDay(name,ending):
     print("Good Day,"+ name)
     print(ending)

goodDay("Atul","Thank you")     


# def sum(a,b,c):
#     print(a,b,c) 

# sum(1,2,3)    


def greet(name):
    gr = "Hello " + name  # Added a space after "Hello"
    return gr

a = greet("Atul")
print(a)  # This will print "Hello Atul"

def tiwari(name,ending):
     print("Goodday"+ name)
     print(ending)
     return "Ok"
# tiwari("Hello","Kavay")

a = tiwari("Hello","Kavay")
print(a)

# By default 
def tiwari_1(name,ending="Thanks"):
     print(f"Good Day,{name}")
     print(ending)

tiwari_1("Viraj","Thank You")
tiwari_1("Kavya")

# Recursion 
 #--- CHAPTER 8 – PRACTICE SET---
#  Write a program using functions to find greatest of three numbers.

def cal(a,b,c):
     if(a>b and a>c):
          return a
     elif(b>a and b>c):
          return b
     elif(c>b and c>a):
          return c
     
a = 1
b = 2
c = 30

print(cal(a,b,c))

#tabale 

def multuply(n):
     for i in range(1,11):
          print(f"{n}x {i}={n*i}")
multuply(5)