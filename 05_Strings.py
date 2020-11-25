# STRINGS ARE COLLECTIONS OF CHARACTERS SEQUENCE IN AN ARRAY
# STRIGNS are 0 indexed based

# STRINGS
a = "Ravinder Brar"
print("variable a is type of " , type(a))
print(a)

# STRINGS ARE OF THREE TYPES:
#1. character quote string
characterQuoteString = 'Str'

#2. Normal String
NormalString = "Normal String"

#3. Multiline Sting
MultilineString = """This is a multiline String
this is a also a multiline String
this is a multiline String"""


# STRING FUNCTIONS AND PROPERTIES -----------------------------------

# printing specifc character of string
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])

# SLICING using [Start Index(included) : EndIndex(Exculded) : character_skip(optional)]

print(a[1:7])
print(NormalString[5:10])
""" we can use negative slicing to start slicing from end of string 
in negative counting start from zero
but the result that will be printed will not in desending
EXAMPLE : """ 

b = "Hello world"
print(b[-5: -2])

c = "RavinderBrar "
print(c[-13:-1])


# if you want to skip character we can do that giving value by giving it as third argument
print(a[::2]) # if you write it will skip 1 character , if you write 3 it will skip 2 character
# if you leave first two paramenter empty and write just :: it mean these have default value of 0:0
# leaving 3rd paramter empty mean that it have its default value of 1 , 1 mean no character will be skipped

print(a[1::3]) # this mean [1 : 0 : 3]
print(a[1::]) # this mean [1 : 0 : 0]
print(a[3:9:4]) # this mean [3 : 9 : 4]
print(a[4::4]) # this mean [4 : 0 : 4]
print(a[::2]) # this mean [0 : 0 : 2]






# LENGTH OF STRING USING len(string)
print(len(a))
print(len(NormalString))
print(len(MultilineString))




#------------ FUNCTIONS -----------------------------------

#   1.  .strip() 
#  remove any white spaces in string from begening or end but not from centre or between words
print(NormalString.strip())

#   2.  .lower()
print(a.lower())

#   3.  upper()
print(a.upper())

#   4.  replace(old value,new value)
print(a.replace("R","P"))
print(a.replace("a","12"))

#   5.  .split()
#   splits the string into substrings if it finds instances of the separator
# return a array

q = "Ravinder , Brar , Singh , Raj"
print(q.split(",")) # here it will seperate every every thing after this comma

# example 2
w = "Bnana - Applw - Mango - Chery"
print(w.split("-"))


#   6 . [in] or[ not in ]
# for checking element is present in or not in string
# in ---
print("Ravi" in a)
# not in
print("Kaur" not in a)


#   7.  +
# concatination
print(a + w)


#   8. FORMAT()
# we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} ar

x = "my name is brar, and i am {} and your name is {} and you are {}"
print(x.format(18,"ravi","20"))


# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 300
price = 10
type_vegi = "Carrot"
name = "Vegitable"
mystr = "these are {3} and these are {1} and there quantity is {0} and price per piece is {2}"
print(mystr.format(quantity, type_vegi, price, name))

# find("value")
# give the first index of given value
print(mystr.find("t"))
print(mystr.find("a"))
print(mystr.find(" "))

