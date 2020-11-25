
""" --------------------- WHILE LOOPS ---------------------------- """
# syntax :--- 
#               while (condtion):
#                       code 
#               or
#
#               while condtion : 
#                       code


# example
i = 0
while i <= 10:
    print("i = ", + i)
    i += 1



""" QUESTION 1 : write a program to print a table of 0 to 20 """
# solution : 
t = 0
while (t <= 20):
    r = 1

    while(r <= 10):
        print(t , "*" , r , " = " , r * t )
        r += 1

    t += 1

