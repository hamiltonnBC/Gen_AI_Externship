################################################################################################
# Assignment: Password Strength Checker
# Name: Nicholas Hamilton
# This project is the sixth assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################






def digit_checker(password):
    for letter in password:
        if letter.isdigit():
            return True

    print('No number in the password!')
    return False


def check_upper(password):

    for letter in password:
        if letter == letter.upper():
            return True

    else:
        print('no upper letter detected!')
        return False

def check_lower(password):
    for letter in password:
        if letter == letter.lower():
            return True

    else:
        print('no lower letter detected!')
        return False


def check_special_characters(password):
    special_letters = ['#','$','@','!']
    for letter in password:
        if letter in special_letters:
            return True
    else:
        print('no special letter detected!')
        return False

def main():
    """
    simple Password Checker

    """
    username = input('what is your username?')
    password = input('what would you like your password to be? to pass all checks, we want'
                     'one upper and one lower case letter, one digit, and one special character like @, #, $ ')

    count = 0
    ## length
    if len(password) < 8:
        print('your password is not long enough!')
    else:
        count += 1

    ## digit present
    if digit_checker(password) == True:
        count += 1

    ## Is upper and is lower
    if check_upper(password) and check_lower(password) == True:
        count += 1

    if check_special_characters(password) == True:
        count +=1

    bonus_points = 0
    if username.lower() in password.lower():
        print("Password should not contain the username. This is bad practice. No bonus points!")
    else:
        bonus_points += 1

    if count == 0:
        print('password is 0/10')
    if count == 1:
        print('password is 2/10')
    if count == 2:
        print('password is 4/10')
    if count == 3:
        print('password is 6/10')
    if count == 4 and bonus_points == 0:
        print('password is 8/10')
    if count == 4 and bonus_points == 1:
        print('password is a 10/10!!!')


if __name__ == "__main__":
    main()













