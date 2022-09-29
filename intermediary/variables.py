# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:59:28 2022

@author: ouedr
"""

# __________________________
"""
This is a comment
written in
more than just one line
"""

# this also a comment

# --------------------------


#What is variables
# variables are objects .they are used to
# refers to a box in our computer memory
# they contains a value,and we can access this
# value by using the variable name
# All the variables are actually an object of a class depending upon the value.

# variables names
# 1 dont start with a digit
# but you can start with a letter(upper or lower case) or an underscore
# myVar, MyVar, _myVar, MyVar123 are valid variable names, but m*var, my-var, 1myVar are invalid variable names.

# int
import numpy as np
a = 4
type(a)

# string
a = "my name"
type(a)

# boolean
statement = True
type(statement())

# remarque
# Unlike other programming languages like C# or Java, Python is a dynamically-typed language,
# which means you don't need to declare a type of a variable.
# The type will be assigned dynamically based on the assigned value.
# you can have access to the adress of this object by using the function
# then python optimize your computer memory for variables with same value

id(a)

# important to notice
# mutilple variable with the same id will have the same id

b = "hello"
id(b)
c = b
id(c)
d = "hello"
id(d)

# Multiple variable assignment
x, y, z = 10, 20, 30
print("x: ", x, "y: ", y, "z: ", z)
x, y, z = 10, 'Hello', True

# x = 10, y = 'Hello', z = True
# variables operation
# lets go with an example
# suppose you're working in a superMrket and store your daily selling
# and at the end the day,they ask differents information

tomatoes = 100
cleaning_stuff = 200
water = 123.23

total1 = tomatoes+cleaning_stuff+water
print(total1)

# still working in a superMarket and now you have to store
# the employers who works this days

employer = " Ami Samyra"
emp2 = "Martin Sanou"
emp3 = "Mr sanfo"


print("todays employers list:", employer, emp2, emp3)

# another way is to use multiple assignment that we use before
employer, emp2, emp3 = " Ami Samyra", "Martin Sanou"

print("todays employers list:", employer, emp2, emp3)

type(emp3)

# third solution
emps = " Ami Samyra,"+"Martin Sanou,"+"Mr sanfo."
print(emps)


# Python Data Types

# Scalar Types

# int
# float
# complex
# boolean
# None

"""lets talks about some operator by using example"""
# /,// (floor division),%to find the remain value of a division
# 2**2 power of a number

"""exercice1:
    Alex and Jean have created a common bank account for their bussiness,
    however after a misunderstanding their decide to split their account 
    and give the remain money to a orphanage.
    if the total amount is 121_0510_871
    1 -how much did Alex receive ?
    2-how much did the orphanage receive?
    After investement in a other business  Jean has doubled is money 
    3-how much have Jean after his investment?
"""


# Sequence Type
# Ordered collection of similar or differnt data


# String
# ==>list of character

"""
eg: 'doesn\'t'
s = 'First line.\nSecond line

eg: path declaration
add r at the beginning means that 
you don't want to consider \ as special character'
print(r'C:\some\name')
print('C:\some\name') 

\n indicate newline
print("""\
#Usage: thingy [OPTIONS]
#     -h                        Display this usage message
#     -H hostname               Hostname to connect to
""")

"""

"""
indexing
we can use slicing to obtain substring
"""

word = "Python Courses"

word[0:1]
word[0:7]
# with negative value slicing start with end's values
word[-1]

# BUT it is not possible to modify  characters of
# words by using slicing that is why we said that string
# are immutable

# count the number of character
len(word)

"""
exercice 2:
additionnal ressource
https://www.tutorialsteacher.com/python/python-string


in my list of clients my first client family name has written
in lowercase i want you to change the first later of his name
to upper.have a look to additionnal ressource you will find the
appropriate function .

name="sanfo"


2-some of the name have upper case but in the wrong place

name2="OueDraogo"  #use the additionnal ressource to correct this
"""

# List
# ==>collection one or more data can be different type of data
""" declare with [] """

l1 = [1, 2, 3, 4]

print(l1[0])

# affectation
l1[0] = 8

print(l1[0])
# pay attention

print(l1*2)

l2 = [9, 2, 1, 12, 11, 0]
l2.sort()

# my bank's clients
mylist = []  # empty list
print(mylist)

names = ["Jeff", "Bill", "Steve", "Mohan"]  # string list
print(names)

item = [1, "Jeff", "ecobank", 75500, True]  # list with heterogeneous data
print(item)


# lets add a new client to our bank
names.append("billy")
print(names)


# Remove Items

"""

"""

del names[0]  # removes item at index 0
print("After del names[0]: ", names)

names.remove("Bill")  # removes "Bill"
print('After names.remove("Bill"): ', names)

print(names.pop(0))  # return and removes item at index 0
print("After names.pop(0): ", names)

names.pop()  # return removes item at last index
print("After names.pop(): ", names)

del names  # removes entire list object
# print(names)


"""
Exercise 3:
    you're' a worker at Ecobank and your boss 
    ask you to help him to manage his clients
    1-create a list containing 4 name of clients
    clients=['Ami','Jean','Paul','Max']
    2-your boss forget one name and ask you to add to
    the list ==> 'Simon'
    
   3- delete Paul from the list 
   4-here is another list 
   list2=["Frank","Mark","Ron","Hermione"]
   add this to your first list "clients"
   
   5-how many clients do you have in you list
   
   
   notice:after each action use print to the result 
   eg: print(clients)
   
    

"""


# tuple are unmutable and there are written with ()
t1 = (1, 2, 3, 4)


a1 = np.array(t1)
print(a1)

# differnce between array and list is that

print(a1*2)


# tuple
# ==>collection one or more data can be different type of data
""" declare with ()"""
t = "hello", "ami", "cava"
tuples = ('hello', 'ami', 'cava')
x, y, z = t

client1 = ("Ouedraogo", "Ami")
client2 = ("Paré", "Fedora")

clist = client1+client2
clist2 = client1, client2

# list in a tuple
v = ([1, 2, 3], [3, 2, 1])

# lets try an example

"""
additional ressources(tuple and dictionnary)
https://www.youtube.com/watch?v=RCM-lVAfXFg&list=PLeo1K3hjS3uv5U-Lmlnucd7gqF-3ehIh0&index=12&ab_channel=codebasics

"""


# Mapping Type

# data

# dict

# Set Types

"""
exercise 4
Coris Bank head director have a list of client in her database ,his use python to have a list
of those client ,but he noticed that some name are used twice ,so he ask your help to him to 
delete duplicate''s names

liste = ['ami', 'john', 'ami', 'pear', 'Max', 'cynthia','Max']
liste[1]=



"""
