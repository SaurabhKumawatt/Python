# operators in python
'''
Operators are used to perform operations on variables and values.
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
'''

# Arithmetic operators
A = 5 + 7
print(A)

a = 10
b = 5

sum = a + b
print(sum)

sub = a - b
print(sub)

multi = a * b
print(multi)

divide = a / b
print(divide)

modules = a%b
print(modules)

expo = a**b
print(expo)

# floor division]
fdiv = a // b
print(fdiv)


# Assignment operators
x = 5
print(x)

# x = x + 5
x += 5
print(x)

# x = x - 2
x-= 2
print(x)

# x = x * 2
x *= 2
print(x)

# Comparison operator
p = 10
q = 10

# equel --- (==)
print(p ==q) # return true bcz p = q = 10

# not equal -- (!=)
print(p != q) # return false bcz p = q = 10

# Greater than
e = 5
f = 7
print(e > f)

#  less than 
print(e < f)

# less than or equal to 
print(e <= f)
# grater than or equal to
print(e >= f)


#  Logical Operators

# and operator --- return true if both are statement true
age = 21
print(age > 18 and age < 25)

# or operator --- return true if one statement is true
value = 25
print(value > 20 or value < 5)
# # returns True because one of the conditions are true (25 is greater than 20, but 25 is not less than 5)

# not operator -- Reverse the result, returns False if the result is true

val = 20
print(not(val > 5 and val < 25)) #returns False because not is used to reverse the result


