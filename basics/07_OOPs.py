
# ---------- OOPs in pyhton ----------
'''Object-Oriented Programming is a way of structuring code around objects (real-world entities) instead of just functions and logic.
        Analogy: Think of a car:

Data → color, speed, model

Behavior → start(), stop(), accelerate()

In Python, we use classes and objects to implement OOPS.
'''
# class student:
#     def __init__(self,name,age):   #constructor, runs automatically when object is created
#         self.name=name             #attributes
#         self.age=age

# S1= student("devyansh",19)
# S2= student("anurag",1)
# print(S1.name,S1.age)
# print(S2.name,S2.age)

# ------- types of constructor -----
'''Default Constructor -->'''

""" Used when you don't need to pass values while creating objects."""
# class Student:
#     def __init__(self):   # default constructor
#         self.name = "Unknown"
#         self.age = 0

# S1 = Student()
# print(S1.name, S1.age)   # Unknown 0

'''Parameterized Constructor--->

Takes arguments to initialize variables dynamically.'''

# class Student:
#     def __init__(self, name, age):   # parameterized constructor
#         self.name = name
#         self.age = age

# S1 = Student("Devyansh", 19)
# S2 = Student("Anurag", 20)

# print(S1.name, S1.age)   # Devyansh 19
# print(S2.name, S2.age)   # Anurag 20

# ----- Methods ---
'''Method is just like a function of calss the just define the behavior of class.'''
'''1. Instance method '''
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name:{self.name} and age is {self.age}")

# S1=student("Devyansh",20)
# S1.display()

'''2.Class method'''
# class Student:
#     school_name = "ABC School"   # class variable
    
#     @classmethod
#     def get_school(cls):
#         return cls.school_name

# print(Student.get_school())   # ABC School

'''3. Static method'''
# class Math:
#     @staticmethod  #decorator
#     def add(a, b):
#         return a + b

# print(Math.add(5, 7))   # 12

# ----- 🔑 Key concept of OOPS -------
# --- 1.Encapsulation --
'''we combine variable + method in class to make data private '''

# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self,amount):
#         self.balance-=amount
#         print(f"Rs {amount} is debited ")
#         print(f"Total balance is {self.balance}")

#     def credit(self,amount):
#         self.balance+=amount
#         print(f"Rs {amount} is credited")
#         print(f"Total balance is {self.balance}")

#     def get_balance(self):
#         return self.balance

# Holder = Account(100000000,83248946)
# Holder.debit(487657)
# Holder.credit(155496871879518499)

# ------- del keyword ---
''' used to delet object details and object property.'''
# class student:
#     def __init__(self,name):
#         self.name = name

# s1=student("devyansh")
# print(s1.name)
# del s1        # here we are deleting the s1 .
# print(s1.name)

# --- Private attributes and methods -----
'''Sometimes we do not want everythig directly accessible out of the class .
            syntax : (Double underscore) __var (Name Mangling)
'''
# class Account:
#     def __init__(self,bal,acc_no):
#         self.__balance = bal
#         self.__account_no = acc_no

#     def debit(self,amount):
#         if (amount>self.__balance):
#             print("Insufficent balance")
#         else:
#             self.__balance -= amount
#             print(f"Rs {amount} is debited")
#             print(f"Remaining balance: {self.__balance}")

#     def get_balance(self):   # public method (accessor)
#         return self.__balance
    
# a1 = Account(1000, 12345)

# print(a1.get_balance())   # ✅ 1000 (allowed)
# print(a1.__balance)       # ❌ Error: Attribute not accessible
