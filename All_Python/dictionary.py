# dictionary in pyhton
# what is dictionary in python ?
# A dictionary is a collection of key-value pairs, where each key is associated
#  with a value. Dictionaries are used to store and retrieve data efficiently.

# Example
# Create a dictionary


marks ={
    "maths": 98,
    "english": 99,
    "science": 97
}

print(marks,type(marks))
print(marks["maths"]) # 98
print(marks["english"]) # 99        
print(marks["science"]) # 97

# ----------------- Method---------------

print(marks.items())
print(marks.keys())
print(marks.values())

print(marks.update({"maths":95 ,"Bhugol":86}))
print(marks)

print(marks.get("maths"))
# print(marks.pop("maths")) 
print(marks)

# -------------

# print(marks["Harry"])# error
# print(marks.get("Harry")) # None


# --------------- Test --------------


Words = {
    "A": "Apple",
    "B": "Ball",
    "C": "Cat",
    "D": "Dog"
}

word = input("Enter a word: ")
print(Words[word])

#  Test 2
s = set()
n = input("Enter a number  1: ")
s.add(int(n))
n = input("Enter a number  1: ")
s.add(int(n))
n = input("Enter a number  1: ")
s.add(int(n))
n = input("Enter a number  1: ")
s.add(int(n))
n = input("Enter a number  1: ")
s.add(int(n))
n = input("Enter a number  1: ")
s.add(int(n))

# Test 3

T = set()
T.add(18)
T.add("18")
print(T)

#  Test 3 ----------

d ={}

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
d.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
d.update({name:lang})

print(d)

print(d["Atul"])