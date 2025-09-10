
# ---------- Functions in pyhton ----------
'''Function are the block of reusable code that perform some specific task and can be use multiple task .
    syntax:
        def function_name(parameters):
            """docstring (optional): explains the function"""
            # function body (statements)
            return value   # optional

'''
# def sum(a,b):  # here def is keyword to define the function and sum is function name
#     sum = a+b
#     print(sum)
#     return sum

# sum(5,10)    
'''here (5,10) are the argument passed in the function and above (a,b)are the parameters.'''

'''return sends a value back from the function.

If no return, Python returns None by default.'''

# ---- Default agrgument ----
# def greet(name="Guest"):          # but here(a,b=2) is valid but (a=2,b)❌ not valid 
#     print("Hello,", name)

# greet()         # Output: Hello, Guest
# greet("Riya")   # Output: Hello, Riya

# ----------------------------------------------------
# heros= ["ironmam","batman","thor","hulk"]

# def hero_call(hero_list):
#     for i in hero_list:
#         print(i, end=" ")

# hero_call(heros) 
# ---------------------------------------------
# -------Recursion function ---------
'''Recursion when the function call itself to slove an problem where it will run until the base conditon occur.
syntax:
                            def recursive_function(parameters):
                                if base_condition:
                                    return value       # always imp to give 
                                else:
                                    return recursive_function(smaller_problem)
                                                
'''
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))
# ---------------------------------------------------------------------

# ------- Some cool python features --------
# -- f string 
'''f-string stand for formatted string literal where insert variables, expressions, and function calls directly inside strings using {}'''
# a , b =5,10
# print(f"{a} + {b} = {a+b}")

# -- Zip
'''Combine multiple lists into pairs (very useful when you need to iterate together).'''

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# -- any() and all() ✅❌
'''Super handy for checking conditions in collections.'''
nums = [2, 4, 6, 8]

print(all(n % 2 == 0 for n in nums))  # True (all even)
print(any(n > 5 for n in nums))       # True (some > 5)
