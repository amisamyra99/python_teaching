# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:33:22 2022
@author: ouedr
"""
# dictinary

"""
python datatype which don't care about order
instead of order ,it's work with a system of key-value '

"""
# we use curly bracket to create a dictionary we have to
# precise the key in the left side of ":" and in the right
# side we give the value
# example
mark = {"English": 12, "German": 12, "Math": 12, "Physics": 12, }

"""
for the first example we chose to work with a string as a key
but we have to know that 
The key should be unique and an immutable object. 
A number, string or tuple can be used as key.

"""

# example
"""
what is an immutable object ?
It is an object that can be modify after is creation
as string ,int and tuples
the opposite of immutable is mutable object
dictionnary ,list ...

"""
# example
# empty dictionary
"""
2 way to create a dictionnary with 
*curly bracket an second is with dict

"""
d = {}
emptydict = dict()
usedict = dict(1="one", 2="two")
# int as key
idClientName = {1: "perez", 2: "Ana", 3: "Ami"}  # int key, string value

# float as a key
decNames = {1.5: "One and Half", 2.5: "Two and Half",
            3.5: "Three and Half"}  # float key, string value

# tuple as a key
companieField = {("Toyota", "Reynolds", "Mercedes"): "vehicules", ("LG",
                                                                   "Whirlpool", "Samsung"): "Refrigerator"}  # tuple key, string value

# Lets try with a list
# this is with give as an error
dict_obj = {["Mango", "Banana"]: "Fruit", ["Blue", "Red"]: "Color"}
# But, a list can be used as a value.
dict_obj = {"Fruit": ["Mango", "Banana"], "Color": ["Blue", "Red"]}

# unique key
# if you have duplicate key the dictionary will
# keep the last key value
numNames = {1: "One", 2: "Two", 3: "Three", 2: "Two2", 1: "One"}

# Acces to dictionnary
"""
Dictionary is an unordered collection, so a value cannot be accessed using an index; instead,
 a key must be specified in the square brackets, as shown below.
"""
idClientName[1]
companieField[("Toyota", "Reynolds", "Mercedes")]

# notice tha key are sensitive and must exist

"""
you can also use get to avoid raising an error when the value don't exist


"""
idClientName.get(1)


# updates a dictionnary
"""
You can change the value of a specific item by referring to its key name

1-affectation
2-by using update function
"""
# Acess to a dictionnary usig
dict_obj["fruit"] = ["pineapple", "orange"]
dict_obj.update({"color": ["red", "white"]})

# add items to a dictionnary
dict_obj.update({"foods": ["burger", "pizza"]})

dict_obj["countries"] = ["burkina", "togo"]

"""
remove dictionnary items

#del dict_obj["countries"]

del dict_obj.pop("countries")

popitem()==>remove the last inserted items

clear() ==> empties the dictionary

"""


# Multi-dimentional Dictionnary

p1 = {"name": "Pr Ouedrao", "age": 67, "course": "Math"}
p2 = {"name": "Pr Traoré", "age": 37, "course": "finance"}
p3 = {"name": "Pr Sanou", "age": 47, "course": "Python"}


professeur = {1: p1, 2: p2, 3: p3}


# acces to a multidimentional key values
professeur[1]
professeur[1]["age"]

# Methods of dictionary


# if statement

num = input(" give us a number:")

if num == 2:
    print("num is 2")
else:
    print("num is not 2")


"""
lets create a list of fruit

fruit=['orange','banana','pineaple','strawberry','mango'] 

"""
fruits = ['orange', 'banana', 'pineaple', 'strawberry', 'mango']
acidefruit = ['lemon', 'orange']

if 'lemon' in fruits:
    print("you have lemon")
elif 'lemon' in acidefruit:
    print("you have lemon")
else:
    print("we don't have lemon")

# statement without else
if 'lemon' in fruits:
    print("you have lemon")
print("we don't have lemon")


# EXERCISE
"""
price = 50
quantity = 5
amount = price*quantity

use if elif else on amount

1_first check if the amount is greater than 0
=>if yes then check if amount is between 3 and 250
==>if no print the amount is negative

"""


# for control block
for i in range(0, 10, 2):
    print(i)


#
for fruit in fruits:
    print(fruit, len(fruit))


# use of while
num = 0
while num < 5:
    num = num + 1
    print('num = ', num)
# double for

""" exercise 2:
    execute and try to understand and explain this code """
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
          # loop fell through without finding a factor
            print(n, 'is a prime number')


# break
'''The execution of the for loop can be stop and exit using the break keyword on some condition, as shown below.'''

for i in range(0, 9):
    if i == 5:
        break
    print(i)


# continue
for i in range(0, 9):
    if i == 5:
        continue
    print(i)


# function
"""
A function is a reusable block of programming statements designed to perform a certain task

"""


def welcome():
    print("welcome to Japan")


"""to call the function
welcome()

"""

"""
the last statement of a function 
is a return statement ,and you can store the value in a 

"""


def welcome(name):
    print("welcome to Japan ", name)
    return name


"""to call the function
welcome("Ami")
or i can 
retrieve the return value 

a=welcome("Ami")
print(a)

"""
# function with parameters


def sum(a, b):
    return a + b


##
# A function in Python can
# have an unknown number of
# arguments by putting * before
# the parameter if you don't know
# the number of arguments the user is going to pass.

"""
The function can have a single parameter prefixed with **. This type of parameter 
initialized to a new ordered mapping receiving any excess keyword arguments, defaulting
 to a new empty mapping of the same type.
"""


def greet(**person):
    print('Hello ', person['firstname'],  person['lastname'])


greet(firstname='Steve', lastname='Jobs')

"""
Exercise 3 on dictionnaries
https://www.w3schools.com/python/python_dictionaries_exercises.asp

to read
https://docs.python.org/3/tutorial/controlflow.html#if-statements

make the quizz number 2
topic:Python variables, data types, functions, list.
https://www.tutorialsteacher.com/online-test/python-test

"""

"""
next session
lambda function
loop with dictionnary
#read,write file
introduction to machine learning

"""
