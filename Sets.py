#Python Sets:
#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List,Tuple, and Dictionary, all with different qualities and usage.
#A set is a collection which is both unordered and not indexed.
#Sets are written with curly brackets.
fruits = {"apple", "banana", "cherry"}
print(fruits)
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.

#Set Items:
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered:
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Unchangeable:
#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.
#Duplicates Not Allowed:
#sets cannot have two items with the same value.
print()
#Duplicate values will be ignored:

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)# apple only printed one time

print()

#Get the Length of a Set:
#To determine how many items a set has, use the len() method.
#Get the number of items in a set:
fruits = {"apple", "banana", "cherry", "apple"}
print(len(fruits))# apple only printed one time and count it as one

#Set Items - Data Types
#Set items can be of any data type:
#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)

#type()
#From Python's perspective, sets are defined as objects with the data type 'set':
#<class 'set'>
my_set = {"apple", "banana", "cherry"}
print(type(my_set))

#Access Items:
#You cannot access items in a set by referring to an index or a key:
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
print()
#Loop through the set, and print the values:
this_set = {"apple", "banana", "cherry"}
for x in this_set:
  print(x)
print()
this_set = {"apple", "banana", "cherry"}
if "apple" in this_set:
  print("apple")

#Change Items:
#Once a set is created, you cannot change its items, but you can add new items.
print()
#Add Items:
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
#Add an item to a set, using the add() method:
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)

print()

#Add Sets
#To add items from another set into the current set, use the update() method.
#Add elements from tropical and this_set into new_set:
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

this_set.update(tropical)

print(this_set)

print()


#Add Any Iterable
#The object in the update() method does not have be a set, it can be any
# iterable object (tuples, lists, dictionaries etc.).
#Add elements of a list to at set:

this_set = {"apple", "banana", "cherry"}
tropical = ["pineapple", "mango", "papaya"]

this_set.update(tropical)
print(this_set)

print()

#Remove Item:
#To remove an item in a set, use the remove(), or the discard() method.
#Remove "banana" by using the remove() method:

this_set = {"apple", "banana", "cherry"}

this_set.remove("banana")
this_set.discard("cherry")

print(this_set)
#Note: If the item to remove does not exist, remove() will raise an error.
#Note: If the item to remove does not exist, discard() will NOT raise an error.
print()
#You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered,
# so you will not know what item that gets removed.
#The return value of the pop() method is the removed item.
#Remove the last item by using the pop() method:
this_set = {"apple", "banana", "cherry"}

this_set.pop()

print(this_set)
#Note: Sets are unordered, so when using the pop() method,
# you do not know which item that gets removed.
print()

#The clear() method empties the set:

this_set = {"apple", "banana", "cherry"}

this_set.clear()

print(this_set)
print()

#The del keyword will delete the set completely:

this_set = {"apple", "banana", "cherry"}

del this_set

#print(this_set) # this will raise an error because the set no longer exists

print()
#Loop Items:
#You can loop through the set items by using a for loop:
#Loop through the set, and print the values:

this_set = {"apple", "banana", "cherry"}

for x in this_set:
  print(x)

print()

#Join Two Sets:
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print()
#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Note: Both union() and update() will exclude any duplicate items.
print()

#Keep ONLY the Duplicates:
#The intersection_update() method will keep only the items that are present in both sets.
#Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

print()

#The intersection() method will return a new set,
# that only contains the items that are present in both sets.
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

print()

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements
# that are NOT present in both sets.
#Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

print()

#The symmetric_difference() method will return a new set, that contains only the elements
# that are NOT present in both sets.
#Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)










