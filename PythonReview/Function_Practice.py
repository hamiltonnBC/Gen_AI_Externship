
################################################################################################
# Assignment: About Parameters of Functions
# Name: Nicholas Hamilton
# This project is the ninth assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################


def greet_user(name):

    print(f'Hello {name}, welcome to the function practice!')


def describe_pet(pet_name='default_dog', animal_type='dog'):
    print(f'My pet is a {animal_type} and its name is {pet_name}.')


def make_sandwich(*args):

    """
    This function takes a list of ingredients and prints them out
    """
    print('Making a sandwich with the following ingredients:')
    for ingredient in args:
        count = args.index(ingredient) + 1
        print(f'{count}. {ingredient}')


def factorial_function(n):
    if n == 1:
        return 1
    return n * factorial_function(n - 1)




def add_numbers(num1, num2):
    """
    This function takes two numbers and returns their sum, simple
    """
    return num1 + num2

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



def main():
    """
    simple function practice

    """

    users_name = input('What is your name? ')
    greet_user(users_name)

    num1 = 5
    num2 = 10
    print(f' the sum of num1 and num 2 is {add_numbers(num1, num2)}')

    # task 2
    pet_name = 'rex'
    animal_type = 'dog'

    describe_pet(pet_name, animal_type)

    make_sandwich('lettuce', 'tomato', 'turkey', 'mayo')

    test_number = 5
    print(f'the factoral of {test_number} is {factorial_function(test_number)}')

    n = 6
    fibonacci_result = fibonacci(n)

    print(f'the {n}th number is {fibonacci_result}')


if __name__ == "__main__":
    main()













