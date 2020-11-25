# OUESTIONS 1 : write a program to two add Number
# solutions : 
a = input("give number 1 \n")
b = input("give number 2 \n")
print(a , "+" , b , "=" , int(a) + int(b))

# OUESTION 2 : write a program to find remaider when a number is divided by 2
# Solution:
c = input("Give one more number \n")
print("remainder when " , c , " is divided by 2 = " , int(c) % 2)

# QUSTION 3 : write a program to check type of variable assigned by using input() functions
# Solution:
d = input("Give any input \n ")

e = int(d)
if e >= 0:
    print("type of ", d , "is = " , type(int(d)))
else:
    print("type of " , d , " is = ", type(d))


# QUESTION 4 : write a program to check is 12 > 34 
print(12 > 34)

# QUESTION 5 : write a python to find average of two numbers entered by users
f = int(input("Give a number \n"))
g = int(input("Give Anoter numer \n"))

print("average of ", f , " and ", g , " is = ", (f + g) / 2) 

# QUESTION 6 : write a python program to calculate square of a number entered by the user
h = int(input("give more number \n"))
print("square root of " , h ," is = " , h * h )



