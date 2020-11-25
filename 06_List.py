# python lists are container to store a set of value of any data ttype
# lists are sorted
# to create a list use [] 
# example

fruits = ["Apple","Mango","Banana","Cherry","Oranges"]
print(fruits)

# lists are 0 index based

# ACCESING SPECIFIC ELEMENT USING INDEX
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# WE CAN CREATE A MIXED LISTS ALSO
Mixed = ["Ravi",12,True,1.11,'C',12121212121]
print(Mixed)

# LISTS ARE MUTABLE : 
# which mean they can be edited later , example --
# editing specifc element at specific index , example list[0]  , list[1] , so..on
fruits[0] = "Bikes"
fruits[1] = "Car"
fruits[3] = "Planes"
print(fruits)



#  LIST METHODS -------------------------------------------

#1.     len(value)
print(len(fruits))

#2.     type()
print(type(fruits))

#3.     we can also create list using  constructor [ list((values))]
Grades = list(('A','C','B','P','F'))
print(Grades)

#4.    clear()
# clears full list
Grades.clear()
print(Grades)

#5.     append()
# add a single elements to the end of list
fruits.append("Carrot")
print(fruits)

#6.     copy()
# return a copy of list
fruits2 = fruits.copy()
print(fruits2)

#7.     count("value")
# returns a number of elements present in the list
print(fruits.count("Car"))

#8.     extend(iterable)
# adds iterable elements to the end of list
# or adds a list to other list
fruits.extend(fruits2)
print(fruits)

#9.     index(element)
# gives the index of item in list
print(fruits.index("Banana"))

#10.    insert(index,value)
# insert a element in the list
fruits.insert(0,"Brar")
print(fruits)

#11.    pop(index)
# removes element at the given index
fruits.pop(1)

#12.    remove(element)
# removes the element from list
fruits.remove("Car")
print(fruits)

#13.    reverse()
# reverses the list
fruits.reverse()
print("this is reverse = ", fruits)

#14.    sort()
# sorts elements of a list
fruits.sort()
print(fruits)


#15. slicing . we can slice list as we do slicing in strings
RollNo = [1,2,3,4,5,6,7,8,9]
print("this is new list ----- ",RollNo)
print(len(RollNo))
print(RollNo[0::2])  # this mean [1:10:2]
print(RollNo[0::3]) # this mean [0:10:3] // here 10 is length of list
print(RollNo[::2])
print(RollNo[-9::],"list")
print(RollNo[-9::1])
print(RollNo[-9:-2:2])


#16.    sum(list)
#returns the sum of members of list
print(sum(RollNo))