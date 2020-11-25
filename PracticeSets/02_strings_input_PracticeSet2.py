
# QUESTION 1 : write a program ti display user entered name followed by goof afternoon using input() function
# SULTION : 
name = input("Please Give your Name \n")
greeting = "Hello {} How are You , Good-After Noon"
print(greeting.format(name))


# QUESTION 2 : write a program to fill in a letter template given below with name and date
""" TEMPLATE : --  Dear <|NAME|> ,
                    Your are Selected for Job I am happy to tell you About your Selection !
                    Your Joining is <|Date|>
                    Have a nice day  """

# SOLUTION :
personName = input("Give your name \n")
Date = input("Enter Date \n")

Letter = '''Dear  <|Name|>  ,
Your are Selected for Job I am happy to tell you About your Selection !
Your Joining is <|Date|>
Have a nice day  '''

Letter = Letter.replace("<|Name|>",personName)
Letter = Letter.replace("<|Date|>",Date)
print(Letter)



# QUESTION 3 : Detect first double spaces in a Letter writen below
# solution :
doubleSpaces = Letter.find("  ")
print("Index of first Doube Spaces in Letter is = " , doubleSpaces)

# QUESTION 4 : replaces of double spaces with single space from letter
print(Letter.replace("  "," "))

# QUESTION 6 : write a program to format the following letter using escape sequence characters.
#  letter = "Dear Brar , This Python Course is Nice , Thanks"
#  now lets format this letter
formatedLetter = "Dear Brar, \n\tThis is Python Course \n Thanks"
print(formatedLetter)

