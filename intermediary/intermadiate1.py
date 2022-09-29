"""
next session
lambda function
 loop with dictionnary
#read,write file
introduction to machine learning
"""
# lambda function


from asyncio.windows_utils import pipe


def add2(x):
    return x+2


# anonymous function
"""
The lambda function can have only one expression. 
Obviously, it cannot substitute a function whose
 body may have conditionals, loops, etc.

"""
# in the following case lambda use to create
# named function as with def


def add2(x): return x+2


def hello(name): return print('hello ', name)


addition = lambda *x: x[0]+x[1]+x[2]
addition(1, 2, 3)


mean = lambda **mark: mark["fr"]+mark["ger"]+mark["Ang"]
mean

# as named functions you can create them without
# parameters
"""
The lambda functions are useful when we want
 to give the function as one of the arguments
  to another function. We can pass the lambda
   function without assigning it to a variable,
    as an anonymous function as an argument to 
    another function.
"""


def normalization(mean, variance):
    m = mean()
    norm = (val-m)/variance
    return norm


normalization(lambda: 1+2+3/3, variance)


# introduction to machine learning

# it also usually use with map, reduce ,and ,filter

# python module presentation

"""
ressources
https://www.tutorialsteacher.com/python/python-module
Module is a way to reuse a code written by someone else

import math

#import a specific function from a module

from functions import sum, average

from functions import *
"""
"""The __name__ attribute returns the name of the module. 
By default, the name of the file (excluding the extension .py)
 is the value of __name__attribute."""

"""
"""
# int pyshell
#import calc
#calc.sum(5, 5)
# calc.__name__
# __name__
#calc.__name__ = "calcul"
# calc.__name__

"""
__doc__
The __doc__ attribute will return a 
string defined at the beginning of the module code.
"""

"""
__file__ is an optional attribute which
 holds the name and path of the module file from which it is loaded.
 import io
>>> io.__file__
"""

"""dir() and dict will return the function and the attribute that you'll need """


"""
Physically, a package is actually a folder containing 
one or more module files.

"""

"""
Python interpreter recognizes a folder as the package 
if it contains __init__.py file."""

"""
install a Package Globally
Once a package is created, 
it can be installed for system-wide use by running the setup script.
 The script calls setup() function from the setuptools module.

 You may also want to publish the package for public use. PyPI

 Visit https://packaging.python.org/distributing
"""
# pip is a package installer
# pip help
# pip list
