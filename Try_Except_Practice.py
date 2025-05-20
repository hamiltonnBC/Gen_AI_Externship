
################################################################################################
# Assignment: Check your Knowledge on Errors
# Name: Nicholas Hamilton
# This project is the 11th assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################




def main():
    """
    simple try except practice

    """
    try:
     user_number = int(input('what number would you like? '))
     print(f' 100 divided by users number is {100 / user_number}')


    except ValueError:
        print('that is not a valid number! ')

    except ZeroDivisionError:
        print("You can't divide by zero!")


    # task 2

    list_of_fruits: list = ['apple', 'banana', 'mango']

    try:
        print(list_of_fruits[4])
    except IndexError:
        print("invalid, too far out of list!")

    me: dict = {'name': 'nick', 'age': 100, 'job': 'programmer'}

    try:
        print(me['hobby'])
    except KeyError:
        print('that key does not exist in that dict')


    example_string = 'hello'
    example_int = 4

    try:
        example_int + example_string
    except TypeError:
        print('cannot add str and int data types! ')

    # task 3



    try:
        user_first_number = int(input('what is your first number? '))
        user_second_number = int(input('what is your second number? '))
        value = user_first_number / user_second_number

    except ValueError:
        print('cannot convert string to integer! ')

    except ZeroDivisionError:
        print('cannot divide by 0!')

    else:
        print(f' the division of these two numbers '
              f'is {user_first_number / user_second_number}')
    finally:
        print('great job!')




if __name__ == "__main__":
    main()













