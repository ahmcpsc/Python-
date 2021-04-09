# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function:
# In Python a function is defined using the def keyword:
def my_function():
    print("Hello, world")


# Calling a Function:
# To call a function, use the function name followed by parenthesis:
def my_function():
    print("Hello, world")


my_function()


# Arguments:#my_function(arguments)
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(name):  # my_function(parameter)
    print("Hello " + name)


my_function("salim")  # my_function(argument)
my_function("ali")


# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# def my_function(name) , so name is parameter
# An argument is the value that is sent to the function when it is called.
# my_function("salim")# my_function(argument)

# Number of Arguments:
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less.
def my_function(name1, name2):
    print("Hello " + name1 + " and " + name2)


my_function("omar", "saleh")

print("\n")


# Arbitrary Arguments, *args:
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*name):
    print("Hello " + name[2])


my_function("omar", "saleh", "saeed")


# Keyword Arguments:
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(student1, student2, student3):
    print("Hello " + student3 + ", hello " + student2 + " and hello " + student1)


my_function(student1="omar", student2="saleh", student3="saeed")


# Default Parameter Value:
# If we call the function without argument, it uses the default value def my_function(name):
def my_function(name="Ali"):  # (name="ali) is the default
    print("Hello " + name)


my_function("omar")
my_function("john")
my_function()  # use the default
my_function("sarah")

print("\n")


# Passing a List as an Argument:
def college(students):
    for each_character in students:
        print(each_character)


names = ["Ali", "Hassan", "Ahmed"]

college(names)


# Return Values:
# To let a function return a value, use the return statement:
def add(x, y):
    z = x * y
    return z


num1 = 6
num2 = 8
result = add(num1, num2)
print("the result of adding two numbers is :", result)


# The pass Statement:
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
# having an empty function definition like this, would raise an error without the pass statement
def my_function():
    pass


# Recursion:
# Python also accepts function recursion, which means a defined function can call itself.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse.
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
def tri_recursion(k):
    if k > 0:
        output = k + tri_recursion(k - 1)
        print(output)
    else:
        output = 0
    return output


print("\n\nRecursion Example Results")
tri_recursion(6)


# another example:
def my_rec(num):
    if num > 0:
        my_result = num + my_rec(num - 1)
        print(my_result)
    else:
        my_result = 0
    return my_result


print("\nrecursion is:")
my_rec(3)


# fact(4):

def x():
    num = int(input("enter a num: "))

    for i in range(num):
        if i == 4:
            print("i is equal to 4")
            break
        print(i)


x()

##
print()


##break:
def x(num):
    for i in range(num):
        if i == 20:
            print("i is equal to 20")
            break
        print(i)


x(50)


##continue:
def x(num):
    for i in range(num):
        if i == 20:
            print("i is equal to 20")
            continue
        print(i)


x(50)

print()


##fact of 3:
def x():
    num = int(input("enter a number: "))
    fact = 1
    rec_num = 1
    for i in range(1, num + 1):
        fact = i * 1
        rec_num *= fact
        print(fact)
    print("the recursion of", num, "is :", rec_num)


x()

print()


##
def x(num):
    fact = 1
    rec_num = 1
    for i in range(1, num + 1):
        fact = i * 1
        rec_num *= fact
        print(fact)
    print("the recursion from the function of ", num, "is :" + str(rec_num))


x(6)


##
def point(x, y, z):
    for i in range(x):
        for j in range(y):
            for k in range(z):
                print("(", i, ",", j, ",", k, ")")


point(3, 4, 5)


# return information from a function:

# here it returns nothing:
def cube(num):
    num * num * num


cube(4)


# here it returns nothing as well, it only prints none:
def cube(num):
    num * num * num


print(cube(4))  # prints none , it returns no value from function


# here it returns something:
def cube(num):
    return num * num * num  # not python gives u back the value


print(cube(4))


# here it returns something:
def cube(num):
    return num * num * num  # not python gives u back the value
    print("hello")  # this code will not print after retun


result = cube(4)
print(result)

print()
# global and local variable in function:
d = int(input("enter num "))  # d is global variable



def add(m, t):
    global d  # d is global but we can change it now
    d = d + 1
    k = 7  # k is locl variable
    print(k)
    print("d inside function is ", d)
    return m + t + d


result = add(8, 4)
print("d outside the function is ", d)

print(result)
