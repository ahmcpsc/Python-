# python numbers:
# Variables of numeric types are created when you assign a value to them:


x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

# 1. Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# 2. Float:
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Complex:
# Complex numbers are written with a "j" as the imaginary part:
x = 3 + 5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# type conversion:
# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number:
# Python does not have a random() function
# to make a random number, but Python has a built-in module called random that
# can be used to make random numbers:

# Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))

# The randrange() method returns a randomly selected element from the specified range.
import random
print("the random number is ", random.randrange(3, 9))
#generate even numbers with steps:
import random
print("the even random number is ", random.randrange(0,100,2))
#generate odd numbers:
print("the odd random number is ", random.randrange(1,100,2))

#randint() function:
#The randint() method returns an integer number selected element from the specified range.
print(random.randint(3, 9))# Return a number between 3 and 9 (both included):

#choice()function:
#The choice() method returns a randomly selected element from the specified sequence.
#The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

#Return a random character from a string:
import random
x = "WELCOME"
print(random.choice(x))

#random() function:
#The random() method returns a random floating number between 0 and 1.
import random
print(random.random())

#shuffle() function:
#The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)# Shuffle a list (reorganize the order of the list items):
print(mylist)

#choice():grap one value from the list
import random
Grades = ["A", "B", "C", "D", "F"]
myGrade = random.choice(Grades)
print("My Grade is ", myGrade)

#choices() to grap list of random values
import random
Grades = ["A", "B", "C", "D", "F"]
myGrades = random.choices(Grades, k=5)# 5 times
print("My Grades is ", myGrades)

#choices() to grap list of random values with different weights
import random
people = ["men", "women", "children"]
results = random.choices(people, weights=[18, 18, 7],k=10)# 10 times
print("My results are ", results)

#print numbers:
print(-2.4+4)

#python casting:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

#the floor division // rounds the result down to the nearest whole number
x = 15
y = 2
print(x // y)

num = -5
print(abs(num))# gives us absolute value
print(pow(num, 2)) # gives us power value
print(max(4, 6)) # gives which number is higher
print(min(4, 6)) # gives which number is amaller
print(round(3.4)) # round it to 3
print(round(3.5))# round it to 4

# import math module to use floor() and ceil()
from math import*
print(floor(3.7))#round the number down
print(ceil(3.7))#round the number up
print(int(sqrt(49)))
print(pi)
print(factorial(6))#6*5*....1=720


















