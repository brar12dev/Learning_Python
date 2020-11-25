""" QUESTION 1 : write a program to create dictionary of hindi words a thier englishtranslation.provide the user with an option to look it up """
# soltuion : 
my_dict = {"Pankha": "Fan",
           "Gadi" : "Car",
           "Jahaj" : "Planes",
           "Dabba" : "Box",
           "Vastu" : "Item"
}

print("Options are", my_dict.keys())
a = input("Enter a Hindi Word\n")
print("Meaning of" , a , " is = " , my_dict.get(a))


"""QUESTION 2 : write a program to input eight numbers from teh user and display all the unique number (once) """
# solution : 
num1 = int(input("Enter Num 1 : "))
num2 = int(input("Enter Num 2 : "))
num3 = int(input("Enter Num 3 : "))
num4 = int(input("Enter Num 4 : "))
num5 = int(input("Enter Num 5 : "))
num6 = int(input("Enter Num 6 : "))
num7 = int(input("Enter Num 7 : "))
num8 = int(input("Enter Num 8 : "))

s = {num1 , num2,num3,num4,num5,num6,num7,num8}
print(s)

""" QUESTION3 : can we have a set that contain 18 a integer and 18 a string and 18.0 , 18.1"""
# lets see this
s2 = {18,"18",18.0,18.1}
print(s2)
print(len(s2))
# soltuions = So the answer is yes , it will contain 18 int and 18 string and 18.1, but not 18.0 as 18 is equal to 18.0

"""QUESTION4 : find the length of set after these expression :
                s3 = set()
                s3.add(20)
                s3.add(20.0)
                s3.add("20")"""
# Sollution
s3 = set()
s3.add(20.0)
s3.add(20)
s3.add("20")
print(s3)
print(len(s3))



"""QUESTION 5 : ceate an empty dictionary , allow 4 friends to ente their favourite language as value and use keys as thier names, assume that the names are unique"""
favlang = {}
a1 = input("Enter your name \n")
print("Enter your favorite language", a1)
a = input()

a2 = input("Enter your name \n")
print("Enter your favorite language", a2)
b = input()

a3 = input("Enter your name \n")
print("Enter your favorite language", a3)
c = input()

a4 = input("Enter your name \n")
print("Enter your favorite language", a4)
d = input()


favlang[a1] = a
favlang[a2] = b
favlang[a3] = c
favlang[a4] = d

print(favlang)


""" QUESTION 6 : if name of 2 friends in QUESTION 5 are same , what will happen to program in Question 5 """
# soltuion : the duplicate key will not be added


""" QUESTION 7 : if language of two friends are same, what will happen to the program in QUESTION 5"""
# solution : the duplicate value will be added ,it will be added nothing will be happened to the program

""" QUESTION 8 : IS THIS set correcct ? ---> {1,2,"singh",[12,23,44,56]} """
# solution : this set is inccorect because we cannot use list in set


""" QUESTION 9 : CAN you change a value from set """
# solution : no because we cannot change any value from set once created