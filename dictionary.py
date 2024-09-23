# dictionary in pyhton

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

print(marks["Harry"])# error
print(marks.get("Harry")) # None