
# ----------- 📕 Dictionary ------------
"""Dictinary are the data type which are used to store the elements in the key:value pair.
    It is mutable and unordered(no index secen  and does not allow to change the key where basically the key are
    in the form of string , tupple or genral primitve data types .
"""
# user={
#     "name":"Devyansh",
#     "password":"karma@333345",
#     "role": "admin",
#     "last_login": "2025-09-04"
# }
# empty={}#Example of empty dictionary.
# # Accesing values
# print(user["name"])
# Adding new key value pair 
# user["email-id"]="devyansh@12345.com"
# updating value 
# user["role"]="superadmin"
# deleting value
# del user["last_login"]
# print(user)
# ---------------------------------------------------------------------------------------------------
# ------------ 📌 Dictionary mehtods ----------------
#Accessing or return the key according to value--->

# print(user.get("role"))# use this instead of below one .
# # user["email"] → ❌ KeyError if key doesn’t exist.
# # user.get("email") → ✅ Returns None or custom default.

# print(user.keys()) # Return all the keys 
# print(user.values()) # Return all the values
# print(user.items())  # Return all the items of key-vlaue pairs 

# Updation and adding new elements 
# user.update({"role":"superadmin","email":"devyansh@1234.com"})
# print(user)

'''The above methods are sufficent for us.'''
# ------------------------------------------------------------------------------------------------------
# ------------💧Sets ---------
'''Sets is the collection of unordered items and in this all elements should be unique and immutable also
    In sets we can't store list and tupples as they are mutable data type .
    In this duplicate values are ignored in ans and were can store multiple data types in a single set.
'''
# set= {1,2,3,4,"devyansh"} # Example of set 
# set_1=set()# Example of empty sets.
# ------------ 📌 Set mehtods ----------------
s = {1, 2, 3}

s.add(4)         # Add a single element
print(s)         # {1, 2, 3, 4}

s.update([5, 6]) # Add multiple elements (list/tuple/set)
print(s)         # {1, 2, 3, 4, 5, 6}

s.remove(2)      # Remove element (❌ KeyError if not found)
s.discard(10)    # Remove element (✅ No error if not found)
print(s)

s.pop()          # Removes & returns a random element and return it , perfer not to use it.
print(s)

s.clear()        # Empties the set
print(s)         # set()

'''some unique methods --->'''
a, b = {1, 2, 3}, {3, 4}
print(a.union(b))        # {1,2,3,4}
print(a.intersection(b)) # {3}

print(a.difference(b))   # {1,2}
print(a.symmetric_difference(b)) # {1,2,4}

x, y = {1,2}, {1,2,3}
print(x.issubset(y))     # True
print(y.issuperset(x))   # True
print(x.isdisjoint({5})) # True
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
