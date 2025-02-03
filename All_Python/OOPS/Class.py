# A class is a blueprint for creating object

class Employee :
    name = "Atul"    # This is a class attribute
    language = "Py"
    Salary = 1200000

Atul = Employee()   
print(Atul.name,Atul.language)

vipul = Employee()
vipul.name = "Vipul"  # This is an insatance  attribute
print(vipul.name,vipul.language,vipul.Salary)

# Insatnce Attribute

class Employee_1:
    Salary = 1200000  # This is a class attribute
    language = "Python"  # This is a class attribute

Viraj = Employee_1()
Viraj.language = "Java Script"  # This is an instance attribute
print(Viraj.language, Viraj.Salary)  # Output: Java Script 1200000  

# ---- Self Method ----------

class Employee_2:
    language = "Python"  # यह एक क्लास एट्रिब्यूट है
    salary = 1200000      # यह भी एक क्लास एट्रिब्यूट है

    def getInfo(self):  # यह इंसटेंस मेथड है An instance method is a function that is part of a class and defines the behavior of an object
        print(f"This Language is {self.language}. The salary is {self.salary}")

# अब हम Employee_2 का एक उदाहरण बनाएंगे:
atul = Employee_2()
atul.language = "JavaScript" # instance Attribute
# और फिर उसे getInfo() मेथड से कॉल करेंगे:

atul.getInfo()
# Employee_2.getInfo(atul)


