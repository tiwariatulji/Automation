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