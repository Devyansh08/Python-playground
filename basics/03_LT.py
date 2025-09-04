
# -------------------- 📃 List in Python ----------------------------------------------------
"""List is like an A list is a collection of ordered, changeable (mutable) items in Python.    
    In this we can store mutiple variables in one places and we can do changes in them.

In list we can not access elements which are out of range .
"""
# mixed_list=["Devyansh",2.25,2,True]
# mixed_list[1]="Karma" # It is mutable
# print(mixed_list)

# ----------------------------------------------------------------------------------------------------------------
# --------- 📌 List methods []---------
# lang=["python","C","Java","Rust","Go"]
# # lang.append("JavaScript") # append() used to add any new thing at last of the list.

# # lang.sort()#sort the list in ascending order
# # lang.sort(reverse=True)# help in arranging in descending orders
# # lang.reverse()#reverse the hole list 
# # lang.extend(["C++","C#"])#used to add multiple things in an list.
# # lang.insert(1,"HTML")#used to insert at an specific index.
# # lang.remove("python")#used to remove the first occurance of the element. 
# # lang.pop(1)#used to remove by index.
# # lang.clear()#used to clear all value from the list.
# '''Above all some methods used in list specially but some string methods are also used in it.'''
# print(lang)
# --------------------------------------------------------------------------------------------------------------------
# --------- 🟢Tuples ()---------
''''Tuple is an ordered collection of elements which are immutables and we cannot change like string
    In this we can use mutliple data type in a single tupple(no .append(), .remove())
'''
# tup=(1,)#single element in tupple , must add a coma for it 
# tup=("Devyansh",2.25,2,True)
# print(tup)
# # ✅ Nested tuple
# # nested = (1, (2, 3), 4)
# # print(nested[1][1])  # 3
# """"Since Tuple is an immutable so it do not have more methods , some are below """
# print(tup.count(2))#count how many times a value has occured 
# print(tup.index("Devyansh"))# Find the first occurance of the value while giving its index.
# ------------------------------------------------------------------------------------------------------------
#-----📝 PRACTICE QUESTIONS-----
""" Q. WAP a program to take input form user of its fav 3 movies and make it into a list?"""
# list=[]
# mov1=input("Enter your first fav movie: ")
# list.append(mov1)
# mov2=input("Enter your second fav movie: ")
# list.append(mov2)
# mov3=input("Enter your third fav movie: ")
# list.append(mov3)
# print(list)
# ----------------------------------------------
""" Q. Check the given list contains a plaindrom of elements or not?"""
list=[1,2,3,2,1]
# copy_list=list.copy()
# copy_list.reverse()
# if(list==copy_list):
#     print("it is a plaindrom ")
# else:
#     print("not an plaindroms")
'''Another way of doing this '''
nums = [1,2,3,2,1]

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
