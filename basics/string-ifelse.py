
# ---------- 🔥 String in pyhton ----------
# name1 = 'Devyansh'
# name2 = "Python"
# name3 = '''This is 
# a multi-line string.'''

# print(name1, name2, name3)
# ----------------------------------------------------------------------------------------------
'''In string indexing alway start from 0 and end on -1'''

'''We use len() function to find the length of an string '''

'''String is an  unmutable data type , we can access the character can't change'''

'''We can use slicing to access the parts of string :
        str[starting index : ending index] here the ending index will not included.
        In negative index also last index is not included 
'''
# name="Devyansh"
# print(name[4:]) # here this line means [2:len(str)] 
# print(name[:3])#[0:3]
# print(name[0:1000]) the answer will be Devyansh only.
# ---------------------------------------------------------------------------------------------
#---------- 💣 String functions ----------
# str = " We are studing string functions "
# print(str.upper()) # used do make all letter capital.
# print(str.lower())     # '  python mentor  '
# print(str.title())     # '  Python Mentor  '

# # 🔹 Removing spaces
# print(str.strip())     # 'Python Mentor'
# print(str.lstrip())    # 'Python Mentor  ' (removes left spaces)
# print(str.rstrip())    # '  Python Mentor' (removes right spaces)

# # 🔹 Replacing 
# print(str.replace("studing","not studing")) #str.replace(old,new)

# #🔹Find
# print(str.find("function"))#finds the 1 index of the 1st occurance

# #🔹Some extra functions 
# print(str.count("ing")) # count the occurance of the substring
# print(str.capitalize())#capitalize the first character.
#---------------------------------------------------------------------------------------------
#---------- 👾 Conditional Statement ----------
'''Basically we have three statements in this 
        1.if -> will always run first and checks the conditon is true or false.
        2.elif -> run when when if conditon get false .
        3. else -> run when all the above conditon get false
We can run multiple if and elif but not else.
'''
# age=99
# if(age<=18 ):
#         print("You are a child play some games.") #always remember of indentation 
# elif(age>=18 and age<60):
#         print("You are an adult live your life")
# elif(age<=99):
#         print("you need to die my friend")
# -----✅ PRACTICE SET ------
'''Take an input from the user and if If the password length is less than 6 → "Weak Password",
if it's between 6-10 → "Medium Password", else → "Strong Password ?"'''

password = input("Please enter your password: ")
if(len(password)<6):
        print("It is a weak password")
elif(6<=len(password)<=10):
        print("It is a medium password")
else:
        print("It is a strong password")

# ----------------------------------------------------------------------------------------------------------------------------------------------