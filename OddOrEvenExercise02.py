'''

Started 8 December 2016
This program was developed in response to the following prompt on PracticePython.org:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

# Start first attempt here

'''

num = int(input("Please provide a number: "))
mod = int(num%2) # This is the first time I've used a modulus. Ever.

if num < 2: # My thought was that 0 and 1 are not odd nor even.
    print("Please provide a different number")

elif mod == 0: # If there is no remainder, the number must be even.
    print("Your number is an even number. How quaint.")

elif mod > 0: # A remainder indicates oddness.
    print("Your number is an odd number. But it's only a phase.")

'''

# End first attempt here.
# This first attempt was successful and satisfies the prompt.

# First attempt at Extras starts here

'''

num1 = int(input("Please provide a number: "))
mod = int(num1 % 2)
mod4 = int(num1 % 4)

if num1 < 2:
    print("Please provide a different number")

elif mod4 == 0:
    print("Your number is an even number, which is also a multiple of four. Well done.")

elif mod == 0:
    print("Your number is an even number. How quaint.")

elif mod > 0:
    print("Your number is an odd number. But it's only a phase.")

num2 = int(input("Please provide another number. "))
check = int(input("Please provide one final number. "))
modredux = num2 % check

if modredux == 0:
    print("Your final number provided divides evenly into the second number you provided.")

elif modredux > 0:
    print("Your final number provided does not divide evenly into the second number you provided.")

'''

# First attempt at the Extras ends here.

'''

What was learned:
1) The modulus' function is to provide a remainder for the division problem of "x/y".
2) if and elif are incredibly useful.
3) You can't have enough variables.
4) This was a lot of fun, and was pretty easily accomplished.

This exercise is complete.

CRF
8 December 2016

'''
