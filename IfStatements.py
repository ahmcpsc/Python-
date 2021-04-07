# Python Conditions and If statements:
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.
a = 33
b = 200

if b > a:
    print("b is greater than a")

# The elif keyword is pythons way of saying "if the previous conditions were not true,
# then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# The else keyword catches anything which isn't caught by the preceding conditions.
x = 3,
y = 50,

if x == y:
    print("hi")
elif x > y:
    print("hello")
else:
    print("bye")

#
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

# The and keyword is a logical operator,
# and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# The or keyword is a logical operator,
# and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested If:
# You can have if statements inside if statements,
# this is called nested if statements.
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# The pass Statement
# if statements cannot be empty, but if you for some reason have
# an if statement with no content,
# put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass

print()


#
def f():
    num = int(input("enter a number: "))
    for i in range(1, num):
        if i % 2 == 0:
            print(i, " is even!")
        else:
            print(i, " is odd!")


f()

print()


#
def f():
    num = int(input("enter a number: "))
    for i in range(1, num):
        if i % 2 == 0:
            print(i, " is even!")
        else:
            print(i, " is odd!")


f()

print()


#
def g():
    import random

    num = random.randint(0, 1)
    win = False
    if num == 0:
        if win:  # means if win is true print, otherwise dont print
            print(num, " is tail!TOU LOST")
    else:
        print(num, " is head!YOU WIN")


g()

print()


##
def marriage(m, t):
    male = m
    tall = t
    if male and tall:
        print(" Sure!I will marry you!")
    elif male or tall:
        print(" Okay!I will think about it")
    elif male and not tall:  # if tall is true then not tall makes it false
        print(" Okay again!I will think about it")
    elif not male and tall:  # if tall is true then not tall makes it false
        print(" Okay again!I will think about it")
    else:
        print("Sorry!I will not marry you!")


marriage(True, False)


# return the biggest number:
def biggest_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


result = biggest_num(700, 387, 487)
print(result)