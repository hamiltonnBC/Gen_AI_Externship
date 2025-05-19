################################################################################################
# Assignment: Exploring String Methods
# Name: Nicholas Hamilton
# This project is the fifth assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################



def task_one():

    print('beginning task 1!')

    s = 'Python is amazing!'

    first_six_letters = s[:6]

    print(f' the first six letters are {first_six_letters}')

    amazing = s[10:17]

    print(f'the last word is {amazing}')

    s_in_reverse = s[::-1]

    print(f'the string in reverse is {s_in_reverse}')


def task_two():

    print('beginning task 2!')
    s = " hello, python world! "

    print(f'original string is {s}')

    stripped = s.strip()

    print(f'stripped is {stripped}')

    print(f' capitalized is {stripped.capitalize()}')

    universe = stripped.replace('world', 'universe')
    print(f' replaced is replaced is {universe}')

    print(f'string upercase is {universe.upper()}')




def task_three(): # treating this as is_palindrome question

    print('starting task 3!')

    s = input('what would you like your word to be? ')

    if s == s[::-1]:
        print(f'{s} is a palindrome!')
    else:
        print(f'{s} is not a palindrome! ')






def main():
    """
    simple assignment to practice string methods and indexing.

    """

    task_one() # prints strings

    task_two() # String methods

    task_three() # palindrome checker


if __name__ == "__main__":
    main()













