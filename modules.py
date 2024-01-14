# Modules in Pyhthon
'''
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''
''' module create 
    def greeting(name):
        print("Hello, " + name)

        saved as a greeting.py
'''

# use a module 
# import module
import myModule
myModule.greeting("Saurabh")

# Variables in Module
# access the person1
age = myModule.person1["age"]
print(age)

name = myModule.person1["name"]
print(name)

# Re-naming a Module
import myModule as my
a = my.person1["age"]
print(a)


'''
# Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
'''

import platform

x = platform.system()
print(x)

y = dir(platform)
# print(y)


# Import From Module
from myModule import person2
age2 = person2["age"]
print(age2)
