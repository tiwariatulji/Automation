# Python Class Methods: Class Vs. Instance Vs. Static Methods
# क्लास विधियाँ (Class Methods) वे विधियाँ हैं जो किसी क्लास (ऑब्जेक्ट) के इंस्टेंस से नहीं बल्कि खुद क्लास से बंधी होती हैं । 
# याद रखें, क्लास में दो तरह की विशेषताएँ होती हैं; क्लास विशेषताएँ और इंस्टेंस विशेषताएँ। 
# क्लास विशेषताएँ क्लास से बंधी होती हैं, जबकि इंस्टेंस विशेषताएँ किसी ऑब्जेक्ट से बंधी होती हैं

#  ---------------------------------------------1.Instance Method -------------------------------------------------
# इंस्टेंस मेथड्स सबसे सामान्य प्रकार के मेथड होते हैं। ये क्लास के एक इंस्टेंस (ऑब्जेक्ट) पर काम करते हैं। ये इंस्टेंस वेरिएबल्स और क्लास वेरिएबल्स दोनों तक पहुँच सकते हैं।

# इंस्टेंस मेथड्स self पैरामीटर लेते हैं, जो कि क्लास के वर्तमान इंस्टेंस को दर्शाता है।

# Example of an Instance Method:

class Employee:
    def __init__(self,name,Salary):
        self.name = name # instance variable
        self.Salary = Salary # instance variable
        
    def get_info(self):
        print(f"Employee Name :{self.name}")
        print (f"Salary :{self.Salary}")

atul = Employee("Atul",120000)

atul.get_info()
# Employee.get_info(atul)

# --------------------------------------- 2.  Class Methods: -------------------------------------------------------
# क्लास मेथड्स क्लास के स्तर पर काम करते हैं, न कि किसी खास इंस्टेंस पर। ये केवल क्लास वेरिएबल्स तक पहुँच सकते हैं, लेकिन इंस्टेंस वेरिएबल्स तक नहीं पहुँच सकते।

# क्लास मेथड्स cls पैरामीटर लेते हैं, जो कि क्लास को दर्शाता है (इंस्टेंस नहीं)।
# इन्हें @classmethod डेकोरेटर के साथ डिफाइन किया जाता है।
# Class Methods Example :

class Employee_2:
    company_name = "Yatra"  # Class variable

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable

    @classmethod
    def get_company_name(cls):  # Class method
        print(f"Company Name: {cls.company_name}")

# Calling the class method without creating an instance
Employee_2.get_company_name()

# Or, you can call it from an instance too
vipul = Employee_2("John", 50000)

Employee_2.get_company_name()

# cls क्लास को संदर्भित करता है, और इसका उपयोग करके आप क्लास वेरिएबल्स (जैसे company_name) तक पहुँच सकते हैं।
# क्लास मेथड को आप सीधे क्लास (जैसे Employee.get_company_name()) या इंस्टेंस (जैसे employee_1.get_company_name()) से कॉल कर सकते हैं।

 # --------------------------------------- Static Methods: --------------------------------------------

# स्टैटिक मेथड्स न तो इंस्टेंस पर काम करते हैं, न ही क्लास पर। ये एक स्वतंत्र फ़ंक्शन होते हैं जो क्लास के अंदर होते हैं, लेकिन ना तो इंस्टेंस वेरिएबल्स को एक्सेस कर सकते हैं और ना ही क्लास वेरिएबल्स को। ये सामान्यत: यूटिलिटी फ़ंक्शन्स के रूप में उपयोग किए जाते हैं।

# स्टैटिक मेथड्स @staticmethod डेकोरेटर के साथ डिफाइन किए जाते हैं।
# ये न तो self लेते हैं और न ही cls।

class Employee_3 :
    @staticmethod
    def calculate_bounus (salary,bonus_percentage): # sataic Method
         return salary * bonus_percentage/100
    
    #Calling the static method without creating an instance
bouns = Employee_3.calculate_bounus(5000,10)
print(f"Bonus:{bouns}")

# स्टैटिक मेथड्स को self या cls की ज़रूरत नहीं होती, क्योंकि ये न तो इंस्टेंस डेटा और न ही क्लास डेटा का उपयोग करते हैं।
# इन्हें आप क्लास (जैसे Employee.calculate_bonus()) या इंस्टेंस (जैसे employee_1.calculate_bonus()) से कॉल कर सकते हैं, लेकिन ये इंस्टेंस या क्लास से कोई डेटा एक्सेस नहीं करते।