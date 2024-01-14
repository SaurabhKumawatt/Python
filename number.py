# There are three numeric types in Python
'''
int  --- whole numbers without decimal
float -- decimal numbers
complex -Complex numbers are written with a "j" as the imaginary part

'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


# Random Number
'''
Python has a built-in module called random that can be used to make random numbers:
'''
# import random module and print number between 1 to 9
import random

print(random.randrange(1, 10))

#  print random number between 1 to 99
print(random.randrange(1, 100))


# print random number between 1 to 1000
randomNumber = random.randrange(1, 1001)
print(randomNumber)