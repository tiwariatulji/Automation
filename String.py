# string is a sequence of characters
# string is immutable
# string is ordered
# string is indexed
# string is defined by single or double quotes

# --------------- String ---------------
name = 'Atul'
print(name)  # string is inmutable
print(len(name))

# --------------- String ---------------
name = "Atul"
print(name)  # string is inmutable
print(len(name))

# --------------- String ---------------
name = '''Atul'''
print(name)  # string is inmutable
print(len(name))
name = "Atul"
print(name)   # string is inmutable
print(len(name))

# String Indexing
print(name[0])  # A
print(name[1])  # t        
print(name[2])  # u 
print(name[3])  # l     
print(name[-1])  # l   
print(name[-2])  # u
print(name[-3])  # t
print(name[-4])  # A

nameshrot = name[0:3]
print(nameshrot)  # Atu
print(name[0:4])  # Atul

# wrod = "amazing"
# word = [:7]  # amazing
# word = [1:]  # amazing
# print(word)  # amazing

# ----------------  String Method -------------
name_1 = "Mahadev"
print(len(name_1))  # 7
print(name_1.upper())  # MAHADEV
print(name_1.lower())  # mahadev
print(name_1.endswith("dev"))
print(name_1.startswith("Dev"))
print(name_1.count("a"))  # 2
print(name_1.capitalize())  # Mahadev
print(name_1.find("v"))  # 4

# ----------------------

string = "abcdefgh"
count = string.count("a")
print(count)  # 1

# -----------------
string2 = "Hello Atul"
change = string2.replace("Atul", "Mahadev")
print(change)  # Hello Mahadev

string3 = "Hello Atul"
print(string3.replace("Atul", "Mahadev"))  # Hello Mahadev

# -----------new line ------------
string4 = "Hello Atul Tiwari\n how are you"
print(string4)  # Hello Atul Tiwari

#------------ F string ------------

name2 = input("Enter your name: ")  
print(f"Good Morning, {name2}")
# --------- Space ---------

name3 ='Good job    atul'
print(name3.find(""))

name4 = "Atul   tiwari  azamgarh "
# print(name4.strip())  # Remove space
print(name4.replace(" ",""))