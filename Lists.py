#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set,
#and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
#List is a collection which is ordered and changeable. Allows duplicate members.

#create a list:
myList = ["apple", "apple", "banana", "cherry"]
print(myList)
print(len(myList))

#list data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]

print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
thisList = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thisList)

#The append() method appends an element to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Add a list to a list:
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

r=["ahmed", "saeed"]
g =["dad"]
r.append(g)
print(r)

#The clear() method removes all the elements from a list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()# Remove all elements from the fruits list
print(fruits)

#The copy() method returns a copy of the specified list.
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()# Copy the fruits list
print(x)

#The count() method returns the number of elements with the specified value.
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")# Return the number of times the value "cherry" appears in the fruits list
print(x)

#Return the number of times the value 9 appears int the list:
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)# Add the elements of cars to the fruits list
print(fruits)

#Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

#The index() method returns the position at the first occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# Note: The index() method only returns the first occurrence of the value.
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

#The insert(pos,element) method inserts the specified value at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")# Insert the value "orange" as the second element of the fruit list
print(fruits)

#The pop(pos) method removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#Note: The pop() method returns removed value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(0)
print(x)

#The remove(element) method removes the first occurrence of the element with the specified value.
#Element: Required. Any type (string, number, list etc.) The element you want to remove
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")# Remove the "banana" element of the fruit list
print(fruits)

#The reverse() method reverses the sorting order of the elements.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()# Reverse the order of the fruit list
print(fruits)

#The reversed(sequence) function returns a reversed iterator object.
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for character in ralph:
  print(character)

#The chr(number) function returns the character that represents the specified unicode.
x = chr(97)
print(x)# output is a

#The sort() method sorts the list ascending by default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()# Sort the list alphabetically
print(cars)

#Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

#Access Items:
#List items are indexed and you can access them by referring to the index number:
thisList = ["apple", "banana", "cherry"]
print(thisList[2])
print(thisList[-1])

#Range of Indexes:
#you can specify a range of indexes by specifying where to start and where to end the range.
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])

#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[:4])

#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
thisList = ["apple", "banana", "orange", "kiwi", "melon", "mango"]
print(thisList[-4:-1])

#Check if Item Exists:
students = ["salim", "saeed", "omar"]
if "omar" in students:
  print("yes")

#Change Item Value:
students = ["salim", "saeed", "omar"]
students[1] = "ali"
print(students)

#Change a Range of Item Values:
students = ["salim", "saeed", "omar"]
students[0:2] = ["ali", "john"]
print(students)

students = ["salim", "saeed", "omar"]
students[0:2] = ["ali", "john"]
print(students)

#The del keyword also removes the specified index:
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

#The del keyword can also delete the list completely.
thisList = ["apple", "banana", "cherry"]
del thisList
#print(thisList) # this will cause an error because you have succsesfully deleted "thislist".

#Loop through a list:
#You can loop through the list items by using a for loop:
family = ["brother", "father", "sister", "mother"]
for character in family:
  print(character)

print("\n")

#Loop Through the Index Numbers:
#Use the range() and len() functions to create a suitable iterable.
family = ["brother", "father", "sister", "mother"]
for i in range(len(family)):# Print all items by referring to their index number
  print(family[i])

#Using a While Loop:
#Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by refering to their indexes.
#Remember to increase the index by 1 after each iteration
family = ["brother", "father", "sister", "mother"]
print(len(family))
i = 0
while i < len(family):
  print(family[i])
  i = i + 1

# make new list: use append()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []
for eachFruit in fruits:
  if "e" in eachFruit:
    newList.append(eachFruit)

print(newList)

#Make a copy of a list with the copy() method:
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(mylist)

#Make a copy of a list with the list() method:
thisList = ["apple", "banana", "cherry"]
myList = list(thisList)
print(mylist)

#Join Two Lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Another way to join two lists are by appending all the items from list2 into list1, one by one:
family1 = ["son", "daughter"]
family2 = ["father", "mother"]

for eachMember in family2:
  family1.append(eachMember)

print(family1)

#Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)




































































