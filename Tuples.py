#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.

#create a tuple:
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

#Unchangeable
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Access Tuple Items:
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1])

#Negative Indexing:
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[-1])

#Range of Indexes:
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[2:5])

#By leaving out the start value, the range will start at the first item:
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[:4])

#This example returns the items from "cherry" and to the end:
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[2:])

#Range of Negative Indexes:
#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[-4:-1])

#Check if Item Exists:
thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change Tuple Values:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y)
print(thisTuple)

#Remove Items:
thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.remove("apple")
thisTuple = tuple(y)
print(thisTuple)

print("\n")

#Loop Through a Tuple:
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
  print(x)

print("\n")
#loop Through the Index Numbers:
thisTuple = ("apple", "banana", "cherry")
for i in range(len(thisTuple)):
  print(thisTuple[i])

#Using a While Loop:
#Print all items, using a while loop to go through all the index numbers:
thisTuple = ("apple", "banana", "cherry")
i = 0
while i < len(thisTuple):
  print(thisTuple[i])
  i = i + 1

#Join Two Tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples:
fruits = ("apple", "banana", "cherry")
myTuple = fruits * 2

print(myTuple)

#The count() method returns the number of times a specified value appears in the tuple.
thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thisTuple.count(5)
print(x)

#Search for the first occurrence of the value 8, and return its position:
thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thisTuple.index(8)
print(x)





























































