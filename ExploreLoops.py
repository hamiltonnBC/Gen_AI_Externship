################################################################################################
# Assignment: Exploring Python Loops
# Name: Nicholas Hamilton
# This project is the third assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project. I have attached the assignment prompt below the code.
################################################################################################


def taskone():

    starting_number: int = int(input('What is your starting number? '))

    if starting_number > 1:

        while starting_number > 0:
            print(f'current number is {starting_number}')
            starting_number -= 1

        print('Blast off!')
    else:
        print('please try writing a number more than 1.')



def tasktwo():


    user_number_for_multiplication = int(input('What is your number for multiplication? '))

    for i in range(11): # could do 1, 11 as well. I am in the habit of not doing this as I switch between languages so often and recalling where step is in range when coding fast doesnt always happen.
        if i == 0:
            continue

        print(f'{user_number_for_multiplication} multiplied by {i} = {user_number_for_multiplication * i}')

def taskthree():

    user_number_for_factorial: int = int(input('What is your number for factorial? '))
    starting_number = user_number_for_factorial

    for num in range(user_number_for_factorial):
        if num == 0: continue

        user_number_for_factorial *= num

    print(f'The factorial of {starting_number} is {user_number_for_factorial}')

def main():

    taskone()
    tasktwo()
    taskthree()




if __name__ == "__main__":
    main()











####################ASSIGNMENT PROMPT############################################################################
# Task 1 - Counting Down with Loops
# Write a Python program to create a countdown timer.
#
# Ask the user for a starting number.
# Use a while loop to print numbers from that number down to 1.
# When the countdown ends, print a celebratory message like "Blast off!"
# For example:
#
# Enter the starting number: 5
# 5 4 3 2 1 Blast off! 🚀
# Task 2 - Multiplication Table with for Loops
# Write a program that generates the multiplication table for any number provided by the user.
#
# Ask the user to input a number.
# Use a for loop to print the multiplication table for that number (from 1 to 10).
# Example Output:
#
# Enter a number: 4
# 4 x 1 = 4 4 x 2 = 8 ... 4 x 10 = 40
# Task 3 - Find the Factorial
# Write a Python program to calculate the factorial of a number entered by the user.
#
# Ask the user for a number.
# Use a for loop to calculate the factorial.
# Print the result in a friendly format.
# For example:
#
# Enter a number: 5
# The factorial of 5 is 120.