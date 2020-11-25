""" TO CREATE A DICTIONARY IN PYTHON WE USE {}
    > syntax of DICTIONARY is {key : value, key2: value, so..on}
    > we can store any type of dataype in dictionary like : list, tuple , string, int etc
    > dictionaries are immutable 
    > you can give a full dictionary as value in a dictionary
    > dictionary are (unordered), it mean we can get element by its index as we do in list
    > it is indexed
    > We cannot use duplicate keys in dictionary
"""

    # lets see example

g = {1,2,}
Grades = {
    "brar" : "A++", # a string
    "me" : 100 , # a integer
    "kiran" : "F-",  # a string
    "mark" : [12,23,34,45,56,67], # a list
    "names" : ("t1","t2","t3","t4"),  # a tupple 
    "words" : {"hello","bye","hi"}, # a dictionary 
}

print(Grades)
print(Grades, "is type of " , type(Grades))

# we can print only value of particular key like this
print("Value of key Me is ",Grades["me"])
print(Grades["mark"])


# mutating the values of keys in dictionary
Grades["brar"] = "Ravinder"
print(Grades)


"""     DICTIONARY METHODS : --------------------------------------------------  """ 

#   1.  .keys()
# gives all keys in dictionary
print(Grades.keys())
# lets check it type
print(type(Grades.keys()))
#  lets convert it into list
print(type(list(Grades.keys())))

#   2.  .values() 
# gives the values of dictionary
print(Grades.values())
print(type(Grades.values()))


#   3.  .items()
# gives the key-value pairs  , we can iterate over it also
print(Grades.items())
print(type(Grades.items()))

#   4.  .update()
# to add a new key-value pair or new dictionary in existing dictionary 
# this can update already existing values also
# example
newDict = {"new" : "old"}
Grades.update(newDict)
print(Grades["new"])
# example 2
newDict2 = {
    "new_list" : ["l1","l2","l3","l4","l5"],
    "names" : "Brar",
    "clases" : ("1st","2nd","3rd"),
    "ranks" : 1,
    "brar" : "ansfaifnpfpwu"  # this will update the value of "brar" instad of making new key value pair
}
Grades.update(newDict2)
print(Grades)


#   5.  .get(key)
# always use this function to get the keys to prevent from errors intead of []
# gives the value of given key ,if present else do not gives error it will give none
# but if you use [] then they will give error if the given key in [] is not present in dictionary
print(Grades.get("new_list2")) # this will give none if given key is not present but will not give error
print(Grades["new_list"]) # this will give error if given key is not present


#  find more methods in https://docs.python.org/3/