
#  Loop in Python

#  while loop
#  for loop
#  nested loop
#  break
#  continue
#  pass

# while loop
# a while loop is used to iterate over a block of code as long as a certain condition is true.

i = 0
while i < 5:
    print(i)
    i += 1
    # Output: 0 1 2 3 4     

# for loop
# a for loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
for i in range(5):
    print(i)    
    # Output: 0 1 2 3 4

# nested loop
for i in range(5):
    for j in range(5):
        print(i, j)         
        # Output: 0 0 0 1 0 2 0 3 0 4 1 0 1 1 1 2 1 3 1 4 2 0 2 1 2 2 2 3 2 4 3 0 3 1 3 2 3 3 3 4 4 0 4 1 4 2 4 3 4 4 4
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(i, j)   
        # Output: 0 0 0 1 0 2 0 3 0 4 1 0 1 1 1 2 1 3 1 4 2 0 2 1 2 2 2 3 2 4 3 0 3 1 3 2 3 3 3 4 4 0 4 1 4 2 4 3 4 4 4

# break
# a break statement can be used to exit a loop or a switch statement.    
# The break statement can be used to exit a loop or a switch statement. The break statement can be used to exit a loop or a switch statement.
for i in range(5):
    if i == 3:
        break
    print(i)
    # Output: 0 1 2

# continue
# a continue statement can be used to skip the rest of the code inside a loop or a switch statement.    
for i in range(5):
    if i == 3:
        continue
    print(i)
    # Output: 0 1 2 4

# pass  
# a pass statement can be used to define a block of code that does nothing.

for i in range(5):
    pass
    print(i)
    # Output: 0 1 2 3 4

# Exercise--------------------

# 1. Write a program to print the following pattern using a loop:
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *   
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
    # Output:
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *


# -----------------------------Exeercies ----------------rcise 2-----------------
# 2. Write a program to print the following pattern using a loop:
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    # Output:
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5

# -----------------------------Exeercies ----------------rcise 3-----------------