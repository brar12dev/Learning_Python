#  SET IS COLLECTION OF WEL DEFINED OBJECTS
""" SETS -------------------------------- 
        > TO CREATE set we use set() function
        > we cannot add copy of  existing elements in set
        > if element already exist and we try to add it again nothing will be added and no error will be given
        > you can create set using {} also , here donot give key-value pairs other wise it will become dictionary
        > if you want to make a empty set use set() function , if you use {} for creating empty set it will form a emoty dictionary
        > SETS are unindexed
        > sets are immutable

"""

s = set()  # this is a empty set
print(type(s))
# other way to make set is
s1 = {11112,2,22,2}
print("type of s1 is = ",type(s1))

#  we can create set from list : like this
list1 = [1,2,3,4,5,6]
s_from_list = set(list1)
print(s_from_list)
print("type of" , s_from_list , " is " , type(s_from_list)) 





""" SET METHODS ----------------------------------------------- """

#1.     .add(value)
# ADDING ELEMENTS TO PREVIOUS EXISITING EMPYT SET OR FULL SET OR ANY SET
s.add(1) # this will add 1 in set named s
s.add(1) # this will not add 1 because 1 is already present in set s , 
s.add(2) # but this will add 2 in set s
s.add (3) # this will also add 3 in set s
s.add("Brar") # this will add brar in set s
s.add("Brar") # this not will add brar in set s , because it already exist
# NOTE : you cannot add list in set using .add() function
# NOTE :  but we can add a tuple using .add function
s.add((12,23,3445))
# NOTE : we can also not add dictionary in set

print(s)

#2       len(set)
# prints length of set
print(len(s))

#3      remove(element)
# remove element at set if present
s.remove((12,23,3445))
print(s)

#4      .pop()
# reomve first element and returns a set
print(s.pop())
print(s) 

#5      .clear()
# clears the set
s.clear()
print(s) # now this set is empty

#6.     .union(other_set)
# returns a new set with all items from both sets
s2 = s1.union(s_from_list) # this will return new set which will contain values of s1 as well as set_from_list sets
print(s2)

#7.     .intersection(other_set)
# return a set whihc contains only those items in both sets 
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,6,7,8}
s3 = set1.intersection(set2)
print(s3)


# for more functions you can check out this : https://docs.python.org/3/