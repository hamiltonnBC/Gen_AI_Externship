
################################################################################################
# Assignment: Calculator
# Name: Nicholas Hamilton
# This project is the 12th assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################


def sum_two_numbers(number1, number2):
    return number1 + number2


def subtract_two_numbers(number1, number2):

    return number1 - number2


def divide_two_numbers(number1, number2):
    while True:
        try:
            return number1 / number2
        except ZeroDivisionError:
            print("Cannot divide by zero! Please enter a new second number.")
            try:
                number2 = float(input("Enter a new second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")



def multiply_two_numbers(number1, number2):
    return number1 * number2


def desired_action(user_choice, number1, number2):
    desired_path = {
        1: sum_two_numbers,
        2: subtract_two_numbers,
        3: multiply_two_numbers,
        4: divide_two_numbers
    }
    return desired_path[user_choice](number1, number2)


def main():
    """
    simple calculator

    """

    user_calculating = True
    available_options = {1, 2, 3, 4}

    while user_calculating:
        try:
            user_choice = int(input("What would you like to do?\n"
                "1: Add\n"
                "2: Subtract\n"
                "3: Multiply\n"
                "4: Divide\n"
                "Enter the number corresponding to your desired action: "
            ))

            if user_choice not in available_options:
                print("Answer must be 1, 2, 3, or 4!")
                continue

            try:
                number1 = int(input("what is your first number?"))
                number2 = int(input("what is your second number?"))

            except ValueError:
                print('please try to enter two numbers that are both actual numbers!')
                continue


        except ValueError:
            print("Invalid input. Please enter a number (1 through 4).")
            continue

        else:
            print(f' your result is {desired_action(user_choice, number1, number2)}')
        finally:
            print('great job!')

if __name__ == "__main__":
    main()













