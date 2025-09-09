
# ---------- ♾️ Loops in pyhton ----------
"""Loops help you repeat tasks automatically (instead of writing the same code 100 times).
    In python we have basically two loops :
        1. while loop ---> runs continusly until condition get false 
        2. for loop .
"""
# ------- while loop ----
# num=1
# while(num<5): # giving the condition 
#     print(num)
#     num+=1    # updation of value 
''' Q. Print table of 9 ?'''
# n=1
# while n<11:
#     print(5*n)
#     n+=1

''' while loop use in list'''
# n=[1,2,3, "devyansh", True]
# x=0
# while x<len(n):
#     print(n[x])
#     x+=1

# ---- Break and Continue---
''' Break --> using this the loop will automatically stop '''
# num=0
# while num<5:
#     print(num)
#     if(num==3):
#         break
#     num+=1

''' continue--> continue terminate the current iteration and jump for the next one in the loop.'''
# num=0
# while num<5:
#     print(num)
#     if(num==3):
#         num+=1
#         continue
#     num+=1


# ------- For loop ----
# list =[1,2,3,4,5]
# for l in list:
#     print(l)

"for with else "
# list =[1,2,3,4,5]
# for l in list:
#     print(l)
# else:           # At the end when our whole loop runs the thing inside the else will print .
#     print("End")

# --- range()---
''' Range return a sequence of number start from 0(by default)  and increased by 1(by default) and stops before a specific number.
        range(start,stop,step)
        and here stop value dena complusory hai.
'''
# for i in range(1,6): # here start is 1 and end 6 
#     print(i) # here it start from 1 and end at n-1=5


# --- pass ---
''' Pass statement is used when we want do nothing in our loop and keep it for future purpose.'''
# for i in range(5):
#     pass 
# print("some thing is remaing for future purpose.")