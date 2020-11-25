var1 = 6
var2 = 56

var3 = int(input("Give a number \n"))

if var3 == var2 or var3 == var1:
    print("equal")

elif var3 > var2 or var3 > var1:
    print("greater")
    

elif (var3 < var2) or (var3 < var1):
    print("smaller")

""" NOTE : YOU CAN USE () OR CAN DIRECTLY GIVE CONDITIONS ARFTER USING IT AFTER WRITING if CONDITION """

list1 = [12,23,34,45,1,2,3,4]

if(var3 in list1):
    print("yes ", var3 , " is present")
else:
    print("no ", var3 , " is not present")


if (var3 in list1) and (12 in list1) :
    print("yes ", var3 , " is present in list 1")
elif var3 in list1 or 12 in list1:
    print("yes ", var3 , " is present in list 1")
else :
    print("not ", var3 , " is not present")
