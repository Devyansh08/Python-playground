print("Welcome to Python playground")

"""
    Some small but key point 👇

    1. we use # for single line comment and '''' or double  for multiline comment .

    2.we use + to add two string manually and ','to add different data type mannually '

    3. Python is case sensitive language, A is no equal to a.
"""
# ----------------------------------------------------------------------------------------------

# name = "devyansh"
# age = 20
# price =0.7
# print(type(name))
# print(type(age))
# print(type(price))
''' we can use type() in this to find the data type of the variables '''
# ----------------------------------------------------------------------------------------------
# ---------- 🔥 Data types in pyhton ----------
"""
1. int      -> whole numbers   a = 10
2. float    -> decimal numbers b = 10.5
3. complex  -> real + imaginary c= 2+3j
4. bool     -> True / False 
5. str      -> text -> way to write string  d = "devyansh" also d = 'devyansh' and d = '''devyansh'''
6.none      -> no value   
Note : This are the basic data types in python, there are other data types like list, tuple, set, dict etc for advance use.
"""
# boolean example 
# a=19 
# print (a>10)  #True 
# print (a<10)  #False
# ----------------------------------------------------------------------------------------------
# ---------- 🔥 Operators in pyhton ----------
"""
1. Arithmetic: +, -, *, /, %, **
2. Comparison: ==, !=, >, <, >=, <=
3. Logical: and, or, not 
4. Assignment: =, +=, -=, *=, etc.
    Advance operators :
5. Membership: in, not in
6. Identity: is, is not
7. Bitwise: &, |, ^, ~, <<, >>

USECASES:
- Arithmetic -> math in ML
- Comparison -> login check
- Logical -> security conditions
- Membership -> restricted lists
- Identity -> object caching
- Bitwise -> cybersecurity, encryption 


Arithmetic Operators → Work with numbers.

Comparison (Relational) Operators → Compare values.

Logical Operators → Combine conditions (True/False).

Assignment Operators → Assign values to variables.

Bitwise Operators → Work on binary numbers (0,1).

Membership Operators → Check if value exists in sequence.

Identity Operators → Check if two objects are the same in memory.

"""
# Some example of operators 
# a = [2,3,4,5,6,]
# b = [5,6,7,8,9,]
# print (a is b ) # Identity operator 
# ----------------------------------------------------------------------------------------------
# ------ 🔥 Type conversion in python 
""" In this we convert one data type to another data type.
    using int(), float(), str(), bool(),etc.
"""
# Example 
# a= "10" #it is string here 
# b= 2 
# sum =int(a)+b
# print(sum)
# ----------------------------------------------------------------------------------------------
# ------ 🔥Input in python 
# name= input("Enter any value: ") #we use it for taking input in python .
# print(name)
# # Always remember that input value will always be in a string , we need to convert them for different data type 
# print(type(name),name)
# ----------------------------------------------------------------------------------------------
# -----✅ PRACTICE SET ------
# a = float(input("Enter some value: "))
# b = float(input("Enter another value: "))
# sum = a + b 
# print(sum)
# ----------------------------------------------------------------------------------------------------------------------------------------------

