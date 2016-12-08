'''

Made 7 December 2016
This program was developed in response to the first prompt on PracticePython.org.
The task is to create a program which asks the user to enter their name and their age.
Then, the program needs to print out a message addressed to them that tells them the year that they will turn 100 years old.

'''

# This was my first program, which satisfies the requirements of the practice problem.
# Remove the block comment to run the program.

'''

name = str(input("What is your name? "))
age = int(input("What is your age, " + name + "? "))
print(name + ", you will turn 100 in the year " + str(2016-int(age)+100) + ".")

'''

# However, this is problematic, as it will not be the year 2016 forever.

'''

import datetime # This imports the module datetime, which allows for time-dependent calculations.
now = datetime.datetime.now() # datetime.datetime.now() pulls the exact moment. now is the variable.
ThisYear = int(now.year) # now.year pulls the year from the exact moment now was calculated. ThisYear is the variable.

name = str(input("What is your name? "))
age = int(input("What is your age, " + name + "? "))
print(name + ", you will turn 100 in the year " + str(ThisYear-age+100) + ".")

# This works and also answers the prompt. This solution is far more robust that the former.

'''

'''

EXTRAS
1) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
2) Print out that many copies of the previous message on separate lines

'''

'''

import datetime # This imports the module datetime, which allows for time-dependent calculations.
now = datetime.datetime.now() # datetime.datetime.now() pulls the exact moment. now is the variable.
ThisYear = int(now.year) # now.year pulls the year from the exact moment now was calculated. ThisYear is the variable.

name = str(input("What is your name? "))
age = int(input("What is your age, " + name + "? "))
message = str(name + ", you will turn 100 in the year " + str(ThisYear-age+100) + ".")

nRepeat = int(input("Please provide a number: "))
for count in range(nRepeat):
    print(message)

# This solution works and answers the prompt in its entirety.

'''

'''
What was learned:
1) Date and time manipulations require importing the timedate module. There are also date and time modules.
2) The input function has an intrinsic print functionality which allows for user input guided by a statement.
3) Even if it seems frivolous, it seems that defining a variable as a string, integer, or a float (I assume) is useful.
4) for loops are really useful.
5) One can examine ranges within variables inside of for loops.

This exercise is complete.

CRF
7 December 2016

'''
