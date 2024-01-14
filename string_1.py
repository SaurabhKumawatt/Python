# Strings and string methods

'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.
ex-- "Saurabh" or 'Saurabh'

'''
print("Saurabh")
print('Saurabh')

# Assign String to variable
name = "Saurabh Kumawat"
print(name)

a = "Indore"
print(a)


# Multiline String 
b = """
 I am Saurabh Kumawat From Indore
 I am learning Python
"""
print(b)

c = '''
I am Saurabh Kumawat From Indore
I am learning Python
'''
print(c)


# string index start from 0
fav = "Chai"
print(fav[0])
print(fav[1])
print(fav[2])
print(fav[3])

# last assign index not count ( ex.--- index 3 is not count )
print(fav[0:4])

d = "I am Saurabh Kumawat"
print(d)
fisrtName = d[5:12]
lastName = d[13:]
print(fisrtName + " " + lastName)

# lenght of string
print(len(d))


# check in string 
print("Saurabh" in d)

if "Saurabh" in d:
    print(True)

# check if not in string    
print("Saurabh" not in d)


# looping strings
for i in "Saurabh":
    print(i)

for i in fav:
    print(i)


# Slicing string
# start and end index
word = "Hello, World!"
print(word[3:5])

# slice from start 
print(word[:5])

# slice to the end
print(word[7:])

# negative index
print(word[-6:-1])

# upper case 
myName = "saurabh kumawat"
print(myName.upper())

# lower case
print(myName.lower())

# capitlize === first letter of word capital
print(myName.capitalize())

# Remove Whitespace
city = "  Indore "
print(city)
print(city.strip())


# Replace String
myFav = "I love Chai"
print(myFav.replace('i', 'ay'))

# split string
print(myFav.split(" "))

# concatenation --- combine two strings
first_name = "Saurabh"
last_name = " Kumawat"
full_name = first_name + last_name
print(full_name)

# String Format -- combine string and numbers
age = 21
# text = "My name is saurabh Kumawat, I am " + age # we got error str cannot concatenate with int
# print(text) 
# inject variable using === {} and format
text = "My name is saurabh Kumawat, I am {}"
print(text.format(age))


quantity = 3
itemno = 567
price = 4995
myorder = "I want {} pieces of item {} for {} Rupees."
print(myorder.format(quantity, itemno, price))

# use index to print right
myNewOrder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myNewOrder.format(quantity, itemno, price)) # it insert values using index
