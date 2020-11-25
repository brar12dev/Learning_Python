# we can take input from user by using a input() function
# this function takes every input as a string
# then we can type to required dataype if type casting is possible

a = input("Enter your Name: \n")
print("your Name is " , a , " and type of a is = " , type(a))

b = input("Enter 2 Number and press ENTER after each number \n")
c = input()

print(b , " + ", c , " = ", int(c) + int(b) , "type of ", b , " and  " , c, " is " , type(int(b)) , type(int(c)))
