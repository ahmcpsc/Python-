#A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).
students = ["ahmed", "jhon", "salim"]
for i in students:
    print(i) # print each student in the students list

#Looping Through a String:
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#The break Statement:
#With the break statement we can stop the loop before it has looped through all the items:
students = ["ahmed", "jhon", "salim"]
for i in students:
    print(i)
    if i == "jhon":
        break # Exit the loop when i is "john":
print()
#Exit the loop when x is "banana",
# but this time the break comes before the print:
students = ["ahmed", "jhon", "salim"]
for i in students:
    if i == "jhon":
        break # Exit the loop when i is "john":
    print(i)    # john will not printed after  break loop
print()
#The continue Statement:
# With the continue statement we can stop the current iteration of the loop,
# and continue with the next:
students = ["ahmed", "jhon", "salim"]
for i in students:
    if i == "jhon":
        continue # continue the loop when i is "john":but it will not print
    print(i)
print()

#The range() Function:
#To loop through a set of code a specified number of times,
# we can use the range() function,
#The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6):
  print(x)

print()
#The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter:
# range(2, 30, 3):
#Increment the sequence with 3 (default is 1):
for i in range(0,11,2):
    print(i)
print()

#Else in For Loop:
#Print all numbers from 0 to 11 increment by 2, and
# print a message when the loop has ended:

for i in range(0,11,2):
    print(i)
else:
    print("end of program.")

print()

#the else block will NOT be executed if the loop is stopped by a break statement.
for i in range(0, 11, 2):
    if i == 8:
        break
    print(i) # it will not execute after the break
else: # will not execute after the break
    print("end of program.")

print()

#Nested Loops:
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":

fruits = ["apple", "banana", "orange"]
years = ["2019", "2020", "2021"]
for f in fruits:
    for y in years:
        print("(", f, ",", y, ")") # print each fruit for each year

print()

#The pass Statement:
#for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass  # having an empty for loop like this, would raise an error without the pass statement





