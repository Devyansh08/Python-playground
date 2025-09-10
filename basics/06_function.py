
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
