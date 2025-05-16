################################################################################################
# Assignment: Number Guessing Game
# Name: Nicholas Hamilton
# This project is the fourth assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################
import random



def main():
    """
    simple number guessing game for externship

    """

    number_to_guess = random.randint(1, 100)
    print('Welcome to the Number Guessing Game!')

    count = 1
    list_of_attempts = []
    while True:

        if count == 11: # starting on count 1

            print(f'that was your 10th attempt! the correct answer was {number_to_guess}.'
                  f'Your guesses were {list_of_attempts}')
            break
        guess = int(input(f'What number would you like to try? 1-100. This is attempt number {count} '))
        list_of_attempts.append(guess)
        if guess > number_to_guess:
            print('Too high, try again! Remember your logarithmic time complexity! ')

        elif (guess < number_to_guess):
            print('Too low, try again! Remember your logarithmic time complexity! ')
        else:
            print(f'Congrats! You passed in {count} attempts! your guesses were {list_of_attempts}')
            break

        count += 1


if __name__ == "__main__":
    main()













