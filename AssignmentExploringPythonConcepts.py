################################################################################################
# Assignment: Exploring Python Concepts
# Name: Nicholas Hamilton
# This project is the first assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project. I have attached the assignment prompt below the code.
################################################################################################


def taskone():

    name: str = 'nicholas' # trying to get in the habit of using type hints most of the time
    age: int = 100
    height: float = 100.50

    print(f'Hello, my name is {name}! I do not give out my age or height, but'
          f' examples are {age} and {height}.') # using f string here


def tasktwo():

    number: int = 1
    number2: int = 2

    sum: float = number + number2

    sum_divided_by_number2: float = sum / number2

    sum_multiplied_by_number2: float = sum * number2

    subtractionExample = number2 - number

    print(f'I made several examples of basic arithmetic operations. here they are:'
    f'{sum}, {sum_divided_by_number2}, {sum_multiplied_by_number2}, {subtractionExample} !')

def taskthree(user_number):

    if user_number > 0:
        print('This number is positive, awesome!')
    elif (user_number < 0):
        print('This number is negative, better luck next time!')
    else:
        print('This number is zero! A perfect balance!')

    return 'task complete!'

def main():

    taskone()
    tasktwo()

    users_number_input = input('What number would you like to test? ')
    user_number = int(users_number_input)
    task_completion_string = taskthree(user_number)



if __name__ == "__main__":
    main()











####################ASSIGNMENT PROMPT############################################################################

# Task 1 - Variables: Your First Python Intro
# Let’s start simple! Imagine you’re describing yourself (or anyone else you like) using Python variables.
#
# Create a name variable that stores a string (like your name or a fictional character’s name).
# Create an age variable that stores an integer value.
# Create a height variable that stores a floating-point number.
# For example, something like this:
#
# name = "Alex"
# age = 25
# height = 5.9
# Now print these variables in a friendly message:
#
# Example Output: "Hey there, my name is Alex! I’m 25 years old and 5.9 feet tall."
# Feel free to get creative with the message! 🚀
#
# Task 2 - Operators: Playing with Numbers
# We all love some math, don’t we? Okay, maybe not everyone, but trust me, this will be easy and fun!
#
# Pick two numbers, let’s say num1 and num2 (you choose the values!).
# Perform the following operations on these numbers:
# Addition
# Subtraction
# Multiplication
# Division
# Write your Python code to calculate and display the results with a nice message for each.
# For example:
#
# num1 = 10
# num2 = 3
# print("The sum of 10 and 3 is", num1 + num2)
# Be sure to explain what you’re doing in comments! Bonus points if you throw in some humor. 😄
#
# Task 3 - Conditional Statements: The Number Checker
# Now for the real challenge: let’s make your code think!
#
# Write a program that takes a number from the user and tells them whether it’s positive, negative, or zero.
# Here’s how it should work:
#
# Ask the user to enter a number (use the input() function).
# Use if, elif, and else statements to check:
# If the number is greater than 0, print: "This number is positive. Awesome!"
# If the number is less than 0, print: "This number is negative. Better luck next time!"
# If the number is exactly 0, print: "Zero it is. A perfect balance!"
# Make sure to test your code with a few different numbers. You’ll be surprised how fun it
# is to see your program come to life! 💻✨
