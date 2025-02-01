# Function is resuable code 
# function is tow type
   # 1. Bulit in function (Already present in Python)
   # 2. user define function (Define by the user)

# a = 1 
# b  = 2
# c = 3 

# average = (a+b+c) / 3
# print(average)

# a = int(input("Enter a number:" ))
# b = int(input("Enter a number:" ))
# c = int(input("Enter a number:" ))

# average_1 = (a+b+c) / 3
              
# print(average_1)

def avg():   # function defination 
    a = int(input("Enter a number:" ))
    b = int(input("Enter a number:" ))
    c = int(input("Enter a number:" ))

    average_1 = (a+b+c) / 3
                
    print(average_1)

avg() # function call

def fun1():
    name = input("Enter Your Name:")
    print("Hello,"+name+"!")
fun1()    

#  ---- ------- Funtion test -------------

def Goodday():
    print("Good Day")
Goodday()    