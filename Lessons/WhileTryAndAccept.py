#Exception Handling
#When an error occurs, or exception as we call it,
# Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement:

#The try block will generate an exception, because x is not defined:
try:
  print(x) # The try block will generate an error, because x is not defined:

except:
  print("An exception occurred")

#Since the try block raises an error, the except block will be executed.
#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:


#Without the try block, the program will crash and raise an error:

#The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# The try block will generate a NameError, because x is not defined:

try:
    print(x)
except NameError:  # Print one message if the try block raises a NameError and another for other errors:

    print("Variable x is not defined")
except:
    print("Something else went wrong")

# The try block does not raise any errors, so the else block is executed:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")








def check_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age > 0 and age < 150:
                if age < 15:
                    print("you are a baby!")
                else:
                    print("you are an adult!")
                return age
                break
            print("invalid age")
        except:
            print("invalid value")


c = check_age()
print("you are age is:", c)

##
import random
head=True
tail=False
def game():
    while True:
        try:
            guess=int(input("Enter number from 1 to 6: "))
            rand_guess=random.randint(0,guess+1)
            print("The random guess is: ",rand_guess)

            if rand_guess== 0 or rand_guess==1:

                if rand_guess == head:
                    print("Congratulation!you win ,your guess is:", head)

                elif rand_guess == tail:
                    print("Sorry,you lost!your guess is:", tail)
                break

            else:
                print("Invalid Value,guess again!")

        except ValueError as error:
            print("Value Error!")

game()

##
import random

grade_p1 = 0
grade_p2 = 0
def game1():
    global grade_p1
    global grade_p2

    try:
        for i in range(6):
            if i%2 == 0:
                p1=int(input("Player1,Choose number from 1 t0 100: "))

                if p1 < 100 and p1 > 1:

                    rand_guess = random.randint(1,p1)
                    print("your random guess is : ",rand_guess)
                    if rand_guess%2 == 0:
                        grade_p1+=1
                        print("player1 grade is:",grade_p1)

                else:
                    print("Invalid number!try again")

            else:
                p2 = int(input("Player2,Choose number from 1 t0 100: "))

                if p2 < 100 and p2 > 1:

                    rand_guess = random.randint(1, p2)
                    print("your random guess is : ", rand_guess)
                    if rand_guess % 2 == 0:
                        grade_p2 += 1
                        print("player2 grade is:",grade_p2)

                else:
                    print("Invalid number!try again")

        print(" player1 grade is",grade_p1," and player2 grade is ",grade_p2)
        if grade_p1 > grade_p2:
            print("Congratulations!Player1 has won.")
        elif grade_p2 > grade_p1:
            print("Congratulations!Player2 has won.")
        else:
            print("witdraw! no winner.")
    except:
        print("invalid Value")
game1()

##
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

##:
while True:
    name = input("> ")
    if name == "ahmed":
        break
    print(name)
print("END PROGRAM!")