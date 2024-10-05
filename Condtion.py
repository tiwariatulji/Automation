# what is condtion in Pyhton ? 
# Ans: The condition in Python is used to check a specific condition or set of conditions 
# and execute the relevant code based on the condition being true or false. It is a fundamental 
# concept in programming and is used in various scenarios, such as conditional statements, loops, and functions.

# Here's an example of how the condition works in Python: 
x = 10         
if x > 5:
    print("x is greater than 5")
    # Output: x is greater than 5
# In this example, the condition x > 5 checks if the value of x is greater than 5. If the condition is true, the code inside the if block is executed, which prints the message "x is greater than 5".

# Here's another example of how the condition works in Python:
age = 20        
if age >= 18:
    print("You are an adult")
    # Output: You are an adult
else:
    print("You are a minor")
    # Output: You are a minor
# In this example, the condition age >= 18 checks if the value of age is greater than or equal to 18. If the condition is true, the code inside the if block is executed, which prints the message "You are an adult". If the condition is false, the code inside the else block is executed, which prints the message "You are a minor".

# Here's another example of how the condition works in Python:
score = 85
if score >= 90:
    print("A")  
    # Output: A
elif score >= 80:
    print("B")
    # Output: B
elif score >= 70:
    print("C")
    # Output: C
else:
    print("F")
    # Output: F



# Note that the if, elif, and else statements are used to create conditional statements in Python. The if statement is used to check a specific condition, the elif statement is used to check multiple conditions, and the else statement is used to execute a block of code when none of the conditions are true.

# Exercise 

a = int(input("input your age "))

if(a>=18):
    print("you can drive")
    # Output: you can drive
elif(a<0):
    print("Your are entenig an invalid age ")

elif(a==0):
    print("you are just born")
else:
    print("you cannot drive")

if(a%2 ==0):
 print("a is even")
   
# PRACTICE SET
#   1.Write a program to find the greatest of four numbers entered by the user.
  
b1 = int(input("Enter your No 1:"))
b2 = int(input("Enter your No 2:"))
b3 = int(input("Enter your No 3:"))
b4 = int(input("Enter your No 3:"))

if (b1>b2 and b1>b3 and b1>b4):
  print("b1 is greatest b1:" ,b1)
  # Output: b1 is greatest b1: 10
elif (b2>b1 and b2>b3 and b2>b4):
  print("b2 is greatest b2:", b2)  
elif (b3>b1 and b3>b2 and b3>b4):
  print("b3 is greatest b3:", b3)
  # Output: b3 is greatest b3: 30
elif (b4>b1 and b4>b2 and b4>b3):
  print("b4 is greatest b4:", b4)

# 2. 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
sub1 = int(input("Enter your marks in subject 1:"))
sub2 = int(input("Enter your marks in subject 2:"))
sub3 = int(input("Enter your marks in subject 3:"))
      # Output: Enter your marks in subject 1:90
      # Enter your marks in subject 2:80
      # Enter your marks in subject 3:70
if(sub1<33 or sub2<33 or sub3<33):
  print("you are Fail because you have less than 33 in each subject")   
  # Output: you are Fail because you have less than 33 in each subject
else:
  print("Congratulation you are pass")
# ---------------------------
if((sub1+sub2+sub3)/3<40):
  print("you are fail due to total percentage less than 40")
  # Output: you are fail due to total percentage less than 40
else:
  print("Congratulation you are pass")


    