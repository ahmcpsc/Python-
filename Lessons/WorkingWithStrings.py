print("Apple pie")
print("Apple\npie")  # use \n to add new line.
# use """    """ as comment for blocks or multi line block

""" 
store the string value in a variable then print the variable
"""
sentence = "Apple cake"
print(sentence)
#
#concatination:tow strings added together
print(sentence+" is nice!")
#
#function:block of code we can run to do specific job
print(sentence.lower()) #convert whole string to lower case.
print(sentence.upper())#change whole sentence to upper case.
print(sentence.isupper())#gives us true or false
print(sentence.upper().isupper())#convert to upper first
print(len(sentence)) #lengh of a string
print(sentence[0]) #grap charaters based on their index
print(sentence.index("A")) #what index is the character
indexSentence = sentence.index("e")
print(indexSentence)
print(sentence.index("ake"))#at what indx starts
print(sentence.replace("cake","pie")) #replace cake with pie
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)#start from index 5 and end at index 10
print(x)

print(txt.count("m"))#count character m in the string
print(txt.count("m",9,15))

txt1 = "my name is {}"
c = txt1.format("Ahmed")#format the string
print(c)

txt2 = "my name is {name} and my age is {age}"
k = txt2.format(name ="salim",age = 30)
print(k)

#Strings are arrays:
a = "Hello, World!"
print(a[1]) #to get charater at position 1

#looping through a string:
welcome = "hello,world"
print(welcome)
print(len(welcome))#11 charaters
for character in welcome: #for Each character in the string weelcome
    print(character,"\n") #will loop 11 times, plus add new empty line at the end

for x in "banana": #for Each x in the string "banana"
    print(x) #will loop 11 times

#check if a certain char or phrase in a string
txt = "The best things in life are free!"
print("free" in txt)# output is true
if "best" in txt:
    print("yes, 'best' is present")

#check if a certian char is NOT in a string:
txt = "The best things in life are free!"
print("ahmed" not in txt)# output is true
x="ahmed"
if x not in txt:
    print("yes, 'ahmed' is not present")

#assign string to a variable
a = "Hello"
print(a)

#assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#both qoutes are correct
print("Hello")
print('Hello')

#slicing string:
m="hello,world" # h has position or index 0
print(m[2:5])#Get the characters from position 2 to position 5 (not included):

#slice from the start:
print(m[:5])#Get the characters from the start to position 5 (not included):

#Slice To the End:
print(m[2:])#Get the characters from position 2, and all the way to the end:

#Negative Indexing:Use negative indexes to start the slice from the end of the string:
b = "Hello, World!" # ! is -1 index
"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
print(b[-5:-2])#

#Modify Strings:

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#Remove whitespace:
#The strip() method removes any whitespace from the beginning or the end:
j = "hello "
print(j.strip())#returns "hello" no space at the end

#Replace string:
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#Split string
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#cout string:
#The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
x = txt.count("ahmed")
print(x)#returns 0
x = txt.count("apple",14,20)#strat at index 14 end at index 20 but not included
print(x)

#Centre String:
#The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(20)
print(x)
#Using the letter "O" as the padding character:
x = txt.center(50, "*")
print(x)

#expand string:
#The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#find string:
#The find() method finds the first occurrence of the specified value.
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
#If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."

print(txt.find("q"))
#print(txt.index("q"))

#rsplit string:
#The rsplit() method splits a string into a list, starting from the right.
#using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
#Split the string into a list with maximum 2 items:
txt = "apple, banana, cherry" # setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x) # note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.

#rstrip string:
#The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
#Remove the trailing characters if they are commas, s, q, or w:
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

#split string:
#The split() method splits a string into a list.
#You can specify the separator, default separator is any whitespace
txt = "welcome to the jungle"
x = txt.split()
print(x)
#Split the string, using comma, followed by a space, as a separator:
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
#Use a hash character as a separator:
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
#Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)
x = txt.rsplit("#", 1)#starts from the right -1 index
print(x)

#loop through split strings:
txt = "apple,banana,cherry,orange"
x = txt.split(",")
print(x)
print(len(x))
for character in x:
    if character=="banana":
        print("hi", character)
        continue
    print(character)

print("\n")

for character in x:
    if character=="banana":
        print("hi", character)
        break
    print(character)
print(x[2])
print(x[3])

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b #Merge variable a with variable b into variable c:
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format strings:
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#You can also use named indexes by entering a name inside the curly brackets {carname}
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#escape characters:
#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "my name is \" ahmed \""
print(txt)

#new line \n:
txt = "my name is\n \" ahmed \""
print(txt)

#make a tab:
txt = "my \tname \tis \" ahmed \""
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.
txt = "orange,apple,banana,grape"
b = txt.split(",")
print(b)
x=",".join(b)
print(x)

mySeperator = "$"
x=mySeperator.join(b)
print(x)

#string string:
#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)























