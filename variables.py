# variables in python

# variable ===>  variable is a reserved memory location to store values
a = 10
name = "Saurabh"
b = 10.5

#  output 
print (a)
print (b)
print (name)

# Get the Type of variables
print (type(a))
print (type(b))
print (type(name))


#  Case-Sensitive 
c = 5
C = 10
# c != C
print (c)
print (C)


#  Single or Double Quotes?
company = 'Microsoft'
company2 = "Google"
# is the same as
print (company)
print (company2)


# typeCasting

x = int('10')
print("i am type of x", type(x)) # i am type of x <class 'int'>

y = str(10)
print("i am type of y", type(y)) # i am type of y <class 'str'>

z = float(10)
print("i am type of z", type(z)) # i am type of z <class 'float'>

# str to int
strVal = "4"
print (type(strVal)) # <class 'str'>

convertInt = int(strVal)
print (type(convertInt)) # <class 'int'>

# int tp str 
intVal = 10
print(type(intVal)) # <class 'int'>

convertStr = str(intVal)
print(type(convertStr)) # <class 'str'>


# variable name 

# Camel case - Each word, except the first, starts with a capital letter
myName = "Saurabh Kumawat"
print(myName)

# Pascal Case --- Each word starts with a capital letter
MyName = "Saurabh Kumawat"
print(MyName)

# Snake Case === Each word is separated by an underscore character
my_name = "Saurabh Kumawat"
print(my_name)


# assign values to multiple variables in one line
firstName, lastName, city = "Saurabh", "Kumawat", "Indore"
print(firstName)
print(lastName)
print(city)

#  the same value to multiple variables in one line
p = q = s = "Python"
print(p)
print(q)
print(s)


# Unpack a Collection --- list, tuple, etc. extract
userDetails = ["Saurabh", "Indore", "Student"]
userName, userCity, userWork = userDetails
print(userName)
print(userCity)
print(userWork)


# Global Variables
Python = "awesome"

def myfunc():
  print("Python is " + Python)

myfunc()


xyz = "awesome"

def myfunc():
  xyz = "fantastic" # local variable i am usaeable in only block scope(inside function)
  print("Python is " + xyz)

myfunc()

print("Python is " + xyz)

# global Keyword === to create gloabl variable

def myfunc():
  global py
  py = "fantastic"

myfunc()

print("Python is " + py)