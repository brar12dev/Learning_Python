""" QUESTION 1 : program to store 7 fruits in a list entered by user """
# SOLUTIONS : 
fruit1 = input("Give fruit 1\n")
fruit2 = input("Give fruit 2\n")
fruit3 = input("Give fruit 3\n")
fruit4 = input("Give fruit 4\n")
fruit5 = input("Give fruit 5\n")
fruit6 = input("Give fruit 6\n")
fruit7 = input("Give fruit 7\n")

# stroing fruits without asking to user
fruits_list = [fruit1,fruit2,fruit3,fruit4,fruit5,fruit6,fruit7]
print(fruits_list)


""" QUESTION 2 : ask user weather he want to enter his input in list or not , and this time create a empty list and then add element to list if user admit to add his input to list"""
#solution : 
new_list = []

print("FOR YESS TYPE [ Y ] AND FOR NO TYPE [ N ]")
permision1 = input("Do you want to add fruit one in list\n")
permision2 = input("Do you want to add fruit two in list\n")
permision3 = input("Do you want to add fruit three in list\n")
permision4 = input("Do you want to add fruit four in list\n")
permision5 = input("Do you want to add fruit five in list\n")
permision6 = input("Do you want to add fruit six in list\n")
permision7 = input("Do you want to add fruit seven in list\n")

if(permision1 == "Y" or permision1 == "y"):
    new_list.append(fruit1)
elif(permision1 == "N" or permision1 == "n"):
    pass

if(permision2 == "Y" or permision2 == "y"):
    new_list.append(fruit2)
elif(permision2 == "N" or permision2 == "n"):
    pass

if(permision3 == "Y" or permision3 == "y"):
    new_list.append(fruit3)
elif(permision3 == "N" or permision3 == "n"):
    pass

if(permision4 == "Y" or permision4 == "y"):
    new_list.append(fruit4)
elif(permision4 == "N" or permision4 == "n"):
    pass

if(permision5 == "Y" or permision5 == "y"):
    new_list.append(fruit5)
elif(permision5 == "N" or permision5 == "n"):
    pass

if(permision6 == "Y" or permision6 == "y"):
    new_list.append(fruit6)
elif(permision6 == "N" or permision6 == "n"):
    pass

if(permision7 == "Y" or permision7 == "y"):
    new_list.append(fruit7)
elif(permision7 == "N" or permision7 == "n"):
    pass

print(new_list)


""" QUESTION 3 : take input from user as his marks and sort them and make a list"""
# solutons : 
mark1 = input("mark 1 = ")
mark2 = input("mark 2 = ")
mark3 = input("mark 3 = ")
mark4 = input("mark 4 = ")
mark5 = input("mark 5 = ")
mark6 = input("mark 6 = ")

marks = [mark1,mark2,mark3,mark4,mark5,mark6]
marks.sort()
print(marks)


""" QUESTION 4 : write a program to summ list elemenst of list """
# solution : 
l1 = [1,2,3,4,5]
print(l1[0] + l1[1] + l1[2] + l1[3] + l1[4])
#or we can use sum() function
print(sum(l1))


""" QUESTION 5 :  write a program to find number of 0 in given tuple"""
# solution 
t1 = (0,2,3,0,0,0,2,3,0)
print(t1.count(0))