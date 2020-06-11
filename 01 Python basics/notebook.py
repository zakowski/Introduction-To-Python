#!/usr/bin/env python
# coding: utf-8

# # Python basics
# 
# Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java.
# 
# Some of Python's notable features:
# 
# - Uses an elegant syntax, making the programs you write easier to read.
# - Is an easy-to-use language that makes it simple to get your program working. This makes Python ideal for prototype development and other ad-hoc programming tasks, without compromising maintainability.
# - Comes with a large standard library that supports many common programming tasks such as connecting to web servers, searching text with regular expressions, reading and modifying files.
# - Python's interactive mode makes it easy to test short snippets of code. There's also a bundled development environment called IDLE.
# - Is easily extended by adding new modules implemented in a compiled language such as C or C++.
# - Can also be embedded into an application to provide a programmable interface.
# - Runs anywhere, including Mac OS X, Windows, Linux, and Unix, with unofficial builds also available for Android and iOS.
# - Is free software in two senses. It doesn't cost anything to download or use Python, or to include it in your application. Python can also be freely modified and re-distributed because while the language is copyrighted it's available under an open-source license.
# 
# Some programming-language features of Python are:
# 
# - A variety of basic data types are available: numbers (floating point, complex, and unlimited-length long integers), strings (both ASCII and Unicode), lists, and dictionaries.
# - Python supports object-oriented programming with classes and multiple inheritances.
# - Code can be grouped into modules and packages.
# - The language supports raising and catching exceptions, resulting in cleaner error handling.
# - Data types are strongly and dynamically typed. Mixing incompatible types (e.g. attempting to add a string and a number) causes an exception to be raised, so errors are caught sooner.
# - Python contains advanced programming features such as generators and list comprehensions.
# - Python's automatic memory management frees you from having to manually allocate and free memory in your code.
# 
# **And most important of all: it is the leading language in Data Science.**

# ## Python code style and naming conventions
# 
# Using the [PEP8 styling guide](https://www.python.org/dev/peps/pep-0008/) fix the code below.

# In[1]:


myVariable = 3.2;
myText = 'Some string';
if (myVariable> 2
   and len(myText) ==11):
    myVariable=0; print( 'This works!');
def _my_function(a,b):
    return (a
            +b);
class my_awesome_object():
    def __init__(self, DESCRIPTION):
        self.DESCRIPTION = DESCRIPTION
        self.sum = _my_function(1,3);
    def __str__ (self):
        return 'self.DESCRIPTION' + str(self.sum)      
x = my_awesome_object('One' + 'Big' + 'String')
print(x);


# If you are interested in the subject of styling and formatting, please check the following resources:
# - [flake8](https://gitlab.com/pycqa/flake8) - a tool to check the style and quality of python code,
# - [Black](https://github.com/psf/black) - automatic python code formatter (read more in [blog post](https://zmudzinski.me/posts/2020/06/black-formatter))
# 
# ### Indentation
# 
# In Python code we won't find popular clamps for separating code blocks from PHP, Java or C #, determining the body framework of a method or class or a set of operations in a loop. Here, specific indentations and blank lines between the abovementioned parts apply. For people who have never had to work with such an organization before the code can be surprising, but it quickly becomes understandable and intuitive.
# 
# ```python
# if score >= 100:
#     print("Victory!")
# ```
# 
# Each subsequent nesting level in the code block is preceded by a space in the form of a multiple of 4 spaces (single indentation). The use of tabs as indentation is also allowed, but spaces are recommended, and in Python 3, the use of spaces and tabs at the same time as indentation is not allowed. Indentation is also used in situations where the code line is too long and must be broken into more lines. The recommended line length according to PEP8 is 79 characters.
# 
# ```python
# sent = send_message(
#     e_mail_of_receiver,
#     message_title,
#     message_body,
# )
# ```
# 
# Declaring variables such as a list, table, tuple or dictionary often induces readability thanks to indentation, which is the main principle that was followed by specifying code formatting rules in Python.
# 
# ```python
# my_list = [
#     1, 2, 3,
#     4, 5, 6,
# ]
# ```
#  
# In case of breaking lines and operators, e.g. arithmetic, the principle of moving the operator to a new line applies.
#  
# ```python
# profit = (
#     income
#     - expense
#     - taxes
# )
# ```
# 
# ### Blank lines
# 
# Separate top-order functions and class definitions from other code blocks with two blank lines.
# 
# ```python
# def do_something():
#     return "done"
# 
# 
# def do_something_else():
#     return "also done"
# ```
# 
# Class methods and local functions are separated by a single blank line.
# 
# ```python
# class Person:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
# 
#     def say_hi(self):
#         print(f"Hello, I'm {self.name} {self.surname}")
# 
#     def my_gender(self):
#         print(f"My gender is {self.gender}")
#         
# 
# me = Person('Lukasz', 'Zmudzinski', 'male')
# me.say_hi()
# me.my_gender()
# ```
# 
# Single blank lines can also be used inside functions to separate logical sections of functions.
# 
# ```python
# def top_level_function():
# 
#     def local_function():
#         pass
# 
#     def another_local_function():
#         pass
# ```
# 
# ### Module importing
# 
# Individual import instructions should be separated into separate lines.
# 
# ```python
# # This is correct:
# import os
# import sys
# 
# # This is horrible:
# import os, sys
# ```
# 
# However, the following way to define an import is correct:
# 
# ```python
# from subprocess import Popen, PIPE
# ```
# 
# When there are many imports from one module, it is worth to replace it this way:
# 
# ```python
# from rest_framework.mixins import (
#     ListModelMixin,
#     CreateModelMixin,
#     RetrieveModelMixin,
# )
# ```
# 
# Imports should be placed at the beginning of the file just after any comments for the module and docstring elements. The order of imports also matters. Here is the recommended order:
# 
# - import of standard libraries
# - import of related external libraries (called third party imports)
# - import of local applications / libraries
# 
# It is also recommended to add an empty line after each of the above import groups. Since Python allows you to import the entire library or only selected modules of it, you often have to choose the right way for the situation, but usually it is recommended to import and add an alias or import a module instead of e.g. a specific class from this module, which reduces the risk of conflicts in space names . For more information and examples, see the chapter on managing and importing packages.
# 
# #### isort
# 
# Recently the [isort package](https://github.com/timothycrosley/isort) is getting a lot of attention. It automatically sorts your imports in a way you want. Be sure to check it out.
# 
# ### Other things
# 
# String variables can be placed either in quotation marks or in single quotes because in Python it does not matter. However, PEP8 does not recommend juggling this entry and sticking to one of the options. A situation where it is allowed to use both at the same time is a text string that itself already contains quotation marks or apostrophe - so use the second one. Each of the following entries is valid:
# 
# ```python
# article = 'Review of "Lord of the Rings".'
# article = "Review of \"Lord of the Rings\"."
# article = """Review of "Lord of the Rings"."""
# ```
# 
# Spaces in expressions and definitions are desirable but should not be abused.
# 
# ```python
# # Good notation
# shopping(meat[1], {eggs: 2})
# x = 1
# my_list[index]
# my_list[1:4]
# 
# # Bad notation
# shopping( meat[ 1 ], { eggs: 2 } )
# x=1
# my_list [index]
# my_list[1: 4]
# ```
# 
# All binary operators should be surrounded by a single space.
# 
# ## Basic data types
# 
# Before we discuss each type of data, it's good to know that Python is a "dynamically typed" language. This means that the type of data that will be used to store the value assigned to a variable often depends on the value that will be assigned to the variable, which is significantly different from the way the types are assigned to variables in Java or C ++.
# 
# This solution has both advantages and disadvantages. The disadvantages include the fact that the original type of the variable may change later in the code, which forces the programmer to have more control over what happens with this variable and sometimes you need to use functions that check the type of data transferred. We can not in any way force the method to pass a specific type of data or specify what type of data will be returned. The advantage of dynamic typing is greater language flexibility and the ability to change the type on the fly, which eliminates the need to explicitly declare new variables to store data in the form of another type (explicit and implicit casting).
# 
# Another important piece of information is that Python is an object-oriented language and everything in Python is an object`*`, which is evidenced by the fact that virtually all variables have methods that can be used on them.
# 
# > `*` - this statement may not be true if you compare object definitions in other programming languages, but from the point of view of Python and its creators is true.
# 
# ### Operators
# 
# Before discussing the types of data, it is worth knowing a few operators that are often used in conjunction with variables.
# 
# ```python
# # Arithmetic
# result = 1 + 2 * 3 / 4.0
# modulo = 12 % 5
# square = 5 ** 2
# cube = 5 ** 3
# 
# # text operations
# full_name = "Lukasz" + " " + "Zmudzinski"
# 
# # What happens here?
# spam = "SPAM " * 10
# print(spam)
# 
# # Lists
# my_list = [1, 2, 3, 4, 5] * 10
# print(my_list)
# 
# # Comparison
# number_1 = 1
# number_2 = 2
# print(number_1 > number_2)
# print(number_1 <= number_2)
# print(number_1 == number_2)
# print(number_1 != number_2)
# 
# # The above comparisons will return boolean values True or False
# # we can also perform operations on logical values
# true = True
# false = False
# print(true and false)
# print(true or false)
# print(not true)
# print(not not true)
# print(bool(true or false))
# ```

# In[2]:


full_name = "Lukasz" + " " + "Zmudzinski"
print(full_name)


# Python performs operations in a specific order in more complex expressions:
# 
# - first `**`
# - then `*`, `/` and `%`
# - the end `+` and `-`
# 
# In Python, the following are treated as false:
# - number zero (0, 0.0, 0j etc.)
# - False
# - None (null)
# - empty collections (`[]`, `()`, `{}`, `set()` etc.)
# - blank inscriptions
# - Objects having the `__bool __ ()` method if it returns False
# 
# ### Numerical types
# 
# Python's two main number types are integer and real, i.e. integer and float. There is also a type of complex that is used to store the value of complex numbers, but I leave the information about it to the reader.
# 
# ```python
# integer = 5
# float = 5.6
# 
# # type casting
# real_number = float(56)
# 
# # and some more examples
# number_str = "123"
# number = int(liczba_str)
# print(type(number))
# 
# # you can also set variables in one line
# # for readability you never do that
# a, b = 3, 4
# ```
# 
# In the case of real numbers, you can also specify the precision with which they will be displayed, but an appropriate example is in the next section.

# In[3]:


# Here you can test out numerical types


# ### Text type
# 
# The code fragments in the previous chapters already contain several examples of variable string type declarations. For example:
# 
# 
# ```python
# article = """Review of "Lord of the Rings"."""
# name = 'Lukasz'
# hobby = "swimming"
# ```
# 
# A text string in Python is an array of characters which gives many possibilities for manipulation and access to components of this string. Another important feature of strings is the fact that after they are declared, we cannot change the declared string characters. Of course, we can overwrite the variable with a new value or add another string to it, but the original fragment does not change. Here are some examples.
# 
# ```python
# name = "Lukasz"
# surname = "Zmudzinski"
# 
# # string is an array of characters so we can refer to its elements
# print(name[0])
# 
# # element index can also be referred to as position from the end of the string
# print(name[-1])
# 
# # you can also get a slice fragment by specifying as an index
# # start and end element. Note the value of these indexes.
# print(name[0] + name[-2] + name[4:5])
# 
# # you can also specify only one of two indexes
# print(name + surname[3:])
# 
# # another way of joining strings
# print(name + " " + surname)
# 
# # String elements cannot be changed so the following statement will return an error.
# surname[0] = "P"
# 
# # Confirmation that the text string is also an object is a possibility to
# # execute methods for this type defined on it. The count() method counts
# # the number of occurrences of a given string in the value stored by the variable.
# print(name.count("k"))
# 
# # Interestingly, in Python we can call functions for a given object already during 
# # the declaration which at first glance may look quite exotic.
# print("You are crazy!".count("a"))
# 
# # Confirmation of invariability of the declared string can also be the following code
# print(name.lower())
# print(name)
# 
# # To return the length of a text string, use the built-in function len()
# print(len(surname))
# ```
# 
# Strings are very often "decorated" with different values before printing to the console. The output string may be a patch of other strings and / or numbers, but we can't just do the following:
# 
# 
# ```python
# print("Ala has " + 4 + " years")
# ```
# 
# The Python interpreter returns an error saying that it cannot perform implicit conversion from type int to string. Below is a listing with the options we have at our disposal.
# 
# ```python
# 
# print("My favourite programming languages are {1} and {0}".format("Swift", "Python"))
# 
# # in the new Python language version it is also possible to refer 
# # to collection items or class fields
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
# 
# person = Person("Lukasz", "Zmudzinski")
# print("The person is {0.name} {0.surname}".format(person))
# 
# ## Or my favourite way from newer Python versions
# print(f'The person is {person.name} {person.surname}')
# ```
# 
# Although the number of examples and methods presented here is quite large and exhausts most of the most common cases, there are still many additional possibilities in the documentation. For more examples, go to the following addresses:
# 
# 1. https://docs.python.org/3/library/string.html#format-string-syntax
# 2. https://pyformat.info/

# In[4]:


# Here you can test out text types


# ### Lists
# 
# The Python list is a collection that can be compared to arrays in other programming languages. An important feature of lists is that they can store different types of data. The size of the array is limited by the capabilities of the equipment. The list can be initialized as follows:
# 
# ```python
# my_list_0 = []
# my_list_1 = list()
# my_list_2 = [1, 2, 3]
# my_list_3 = ["a", 5, "Python", 7.8]
# ```
# 
# The elements of the list are referred to in the same way as the elements of the text string because there we also deal with the list (although these are string objects).
# 
# We can also put lists in a list, which gives us multi-level lists.
# 
# ```python
# my_list_4 = [my_list_2, my_list_3]
# ```
# 
# In Python, you can also easily combine lists:
# 
# ```python
# my_list_2.extend(my_list_3)
# print(my_list_2)
# ```
# 
# Or an easier (better) way:
# 
# ```python
# my_list_6 = my_list_2 + my_list_3
# print(my_list_6)
# ```
# 
# Both methods differ from each other in that the first modifies an existing list, and the second requires substitution of the combined list for a variable, as the arithmetic operation `+` alone will not change the original list.
# 
# Some methods that can be performed on the list object are performed as in-place operations, which means that the operation is performed without returning a new value, so you cannot assign the changed array to another variable. Below is an example with sorting:
# 
# ```python
# my_list_7 = [7, 9, 3, 1]
# sorted_list = my_list_7.sort()
# print(my_list_7)
# print(sorted_list)
# ```
# 
# The `None` value in Python corresponds to the Null value in other programming languages. We also can't sort the array with numbers and text strings.
# 
# Lists can be "sliced" just like the text strings presented in the previous chapter.
# 
# Adding, removing and changing the value of list elements can be done in many ways. Listing below with some of them.
# 
# ```python
# # creating a list
# scale = [1, 2, 3, 4, 5]
# 
# # adding a new element
# scale.append(6)
# print(scale)
# 
# # we already know how to refer to a list item through an index so you can
# # set the list values in this way, but you cannot put values on
# # an index that does not exist
# scale[6] = 7
# 
# # you will get an exception IndexError: list assignment index out of range
# # but you can do it e.g.
# scale[6:] = [7]
# 
# # or like this
# scale[len(scale):] = [7]
# 
# # an alternative way is to call the insert method
# scale.insert(6, 7)
# print(scale)
# 
# # we remove an item from the end of the list which makes using
# # of these methods we achieve the stack function
# scale.pop()
# print(scale)
# 
# # pop can also take the index of an item to delete.
# # The pop method also returns the value of the removed item
# scale.pop(2)
# print(scale)
# ```
# 
# You can also use the built-in `del()` function to delete list items, which returns no value. You can also use it to delete variables.
# 
# This chapter introduces the basics of list operations. Python offers many more powerful options for generating, selecting, and sorting lists, but concepts such as loops and conditional statements must first be introduced. In the documentation, you can also find examples using the lambda instruction, but its use will be discussed in more detail during advanced Python classes.

# In[5]:


# Here you can test out lists


# ### Tuples
# 
# Tuples are very similar to lists, except that they are an invariant type and the declaration of variables is written in parentheses rather than square brackets. They can also store many types of data at the same time.
# 
# ```python
# # Creating a tuple
# my_tuple = (1, 2, "Jacek", "ma")
# number_tuple = my_tuple[:2]
# print(number_tuple)
# 
# text_tuple = my_tuple[2:]
# print(text_tuple)
# 
# new_tuple = tuple()
# even_more_new_tuple = tuple([1, 2, 3])
# 
# # we can also cast tuple - list types
# my_list = [1, 2, "Ala", "też", "ma"]
# tuple_from_list = tuple(my_list)
# new_list = list(tuple_from_list)
# 
# # tuples can be nested
# big_tuple = text_tuple, number_tuple, tuple(new_lista)
# print(big_tuple)
# 
# # What if we nest the list in a tuple?
# list_tuple = tuple_from_list, new_list
# 
# # then we can still modify the list items
# list_tuple[1][0] = 0
# print(list_tuple)
# 
# # tuple packing and unpacking
# t = 5, 6, 7
# print(t)
# x, y, z = t
# 
# # another way of combining variables of different types in string
# print("x = " + str (x))
# print("y = " + repr(y))
# print("z = " + str(z))
# ```

# In[49]:





# ### Dictionaries
# 
# Dictionaries are a hash table that can be compared to associative tables known from other programming languages. Dictionaries store key: value pairs and the key is searched. The key in the dictionary can be any fixed data type, e.g. string or number. A tuple can also be a key if it contains invariant types (string, number, tuple). The keys in the dictionary are unique and the element pairs are not ordered in the order in which they were added. The dictionary has already been used in previous examples in the section on formatting text strings.
# 
# Below are the code snippets creating a dictionary and showing how to access its data.
# 
# ```python
# # creating a dictionary
# my_dict = {}
# my_dict = dict([
#     ("one", 1),
#     ("two", 2),
#     ("three", 3),
# ])
# 
# my_dict = dict(one=1, two=2, three=3)
# my_dict = dict({
#     "one": 1,
#     "two": 2,
#     "three": 3,
# })
# 
# my_dict = {
#     "one": 1,
#     "two": 2,
#     "three": 3
# }
# print(my_dict["one"])
# 
# # Checking if key is in dictionary
# print("one" in my_dict)
# 
# # Writing out all keys
# print(my_dict.keys())
# 
# # Writing out all values
# print(my_dict.values())
# 
# # We can also check if a key is present in this way
# # but it is slowe than the one before
# print("one" in my_dict.keys())
# 
# # Adding a new dictionary item
# my_dict["four"] = 4
# print(my_dict.keys())
# ```

# In[7]:


# Here you can test out dictionaries


# ### Sets
# 
# The set is an unordered collection whose important feature is that it contains unique elements (i.e. without repetitions). The sets also support mathematical operations that are known from set theory: sum, intersection, difference and symmetrical difference.
# 
# ```python
# # Init of a set
# people = {"Marek", "Janek", "Ania", "Ewa", "Marek", "Ania"}
# print(people) # no duplicates
# 
# # And now a set from a string
# char = set("czabunagunga")
# print(char)
# 
# dif_char = set("abrakadabra")
# print(dif_char)
# 
# print(char - dif_char) # in char but not in dif_char
# print(char.difference(dif_char)) # the same as above
# print(dif_char - char) # not the same, as in theory
# 
# print(char | dif_char) # characters in char or dif_char or both
# print(char & dif_char) # intersection
# print(char.intersection(dif_char)) # the same as above
# print(char ^ dif_char) # symetrical difference
# ```
# 
# Ownership of the unique elements of the set becomes very useful if we want to eliminate duplicates from the list, because it is enough to cast the list to the set and the matter settled, and then, if we need the list again at the output, we project in the opposite direction.

# In[8]:


# Here you can test out sets


# ### The `range()` function
# 
# The function (although to call it more precisely the invariant sequence) range is used to generate a series of numbers according to given parameters. It is often useful in loops or when creating lists or sets of numbers. `The range()` function and the way it was used changed during the development of the language and its use in Python 2.x differs from what will be presented here. I leave the details to the reader.
# 
# The following code snippets show how the range function works.
# 
# ```python
# from decimal import *
# 
# # What is the type of range?
# numbers = range(5)
# print(type(numbers))
# 
# # If you add one parameter, its the stop parameter
# for i in range(10):
#     print(i)
# 
# # But range can take 2 parameters (start, stop)
# for i in range(4, 10):
#     print(i)
# 
# # Or three parameters (start, stop, step)
# for i in range(4, 10, 2):
#     print(i)
# 
# # We can also generate negative values
# for i in range(-5, -1):
#     print(i)
# for i in range(-5, -10, -2):
#     print(i)
# 
# # A list from range elements
# number_list = list(range(10))
# print(number_list)
# 
# # Function range doesn't create float values, but
# # we can easily create such a function
# def frange(start, stop, step):
#     i = start
#     while i < stop:
#         yield i
#         i += step
# for i in frange(0.1, 0.5, 0.1):
#     print(i)
# 
# # After displaying the result, it's not really what we wanted
# # So maybe once again but like this:
# for i in frange(0.1, 0.5, 0.1):
#     print(Decimal(i))
#     
# print((0.1 + 0.2) == 0.3)  # Oh my, not exactly what we wanted
# print(round((0.1 + 0.2), 2) == round(0.3, 2))  # Now better
# 
# print((Decimal(0.1) + Decimal(0.2)) == Decimal(0.3))
# print((Decimal('0.1') + Decimal('0.2')) == Decimal('0.3'))
# ```

# In[9]:


from decimal import *

numbers = range(5)
print(type(numbers))

for i in range(10):
    print(i)


# # Exercises
# 
# Download the paragraph text "What is Lorem Ipsum" from https://pl.lipsum.com/ and assign it to a variable.

# In[10]:


myText='Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker';

print(myText)


# Return from cell the text `"In the text there are {letter_1} letters from name and {letter_2} letters from surname"`. In place of `{}` substitute variables that will store the number of occurrences of given letters. The letters to be searched should as an index to the 3rd character of the surname and the 2nd character of the first name of the person performing the exercise, e.g. Use the paragraph text from previous cell.
# 
# ```python
# name = "Lukasz"
# surname = "Zmudzinski"
# letter_1 = name[1]
# letter_2 = surname[2].
# ```

# In[11]:


name = 'Lukasz'
surname = 'Zakowski'

letter_1 = name[1]
letter_2 = surname[2]

result1 = 0;
result2 = 0;

for i in myText:
    if(i == letter_1):
        result1 +=1
    if(i == letter_2):
        result2 +=1
        
print(myText.count(letter_1))
print(myText.count(letter_2))

        
print("In the text there are ", result1," letters from name and " , result2, " letters from surname",)
    


# Go to https://pyformat.info/ and copy 5 selected examples of string formatting marked "New", which were not in the examples in this section (e.g. with alignment, number of positions, mark etc.).

# In[12]:


print('{:>10}'.format('test1'))

print('{:_<10}'.format('test'))

print('{:.5}'.format('xylophone'))

print('{:4d}'.format(42))

person = {'first': 'Jean-Luc', 'last': 'Picard'}

print('{p[first]} {p[last]}'.format(p=person))


# Search the Internet for "extended slice" in the Python context and display your name in reversed order with small caps. E.g. `Iksnizdumz Zsakul`

# In[21]:


print(name +" "+ surname)
NS = name + " " + surname

print(NS[::-1])


# Create a list with values from 1 to 10. Then divide the list so that the first 5 numbers remain in the original list and the remaining 5 are in the new list.

# In[42]:


my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)

my_list2 = my_list[5:10]
print("new ", my_list2)

del my_list[5:10]
print("original ", my_list)



# Link these lists again. Add `0` to the list first. Make a copy of the combined list and display the list sorted in descending order.

# In[43]:


my_list.append(0)
my_list = my_list + my_list2

print(my_list)

my_list3 = my_list
my_list3.sort(reverse=True)

print(my_list3)


# Use the tuples to create a list of students in your group by assigning an `index number` to `name` (the data does not have to be true).

# In[60]:


s1 = (132123 , "Pawel Noga")
s2 = (111222 , "Adam Spadam")
s3 = (222333 , "Monika Kicha")
s4 = (231231 , "Jakub Wielki")
s5 = (444111 , "Bartosz Zbigniewski")

list_of_students = s1,s2,s3,s4,s5

#print(list_of_students[2][0])

print(list_of_students)


# Convert your previous assignment to a dictionary, then add pairs containing age, email address, year of birth and address (data does not have to be true).

# In[ ]:


# Your code here


# Create a list of phone numbers with repetitions, and then delete the repetitions by casting to `set`.

# In[ ]:


# Your code here


# Using the `range` function, list items ascending from 1 - 10

# In[ ]:


# Your code here


# Using the `range` function, write items descending from 100 - 20, every 5 values.

# In[ ]:


# Your code here


# Combine all the knowledge obtained from the classes (and tasks) and create a program that writes data from a list that contains several dictionaries (write the data in the form of one string, formatting it accordingly).

# In[ ]:


# Your code here

