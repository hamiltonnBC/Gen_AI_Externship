################################################################################################
# Assignment: Eligible Elector
# Name: Nicholas Hamilton
# This project is the second assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project. I have attached the assignment prompt below the code.
################################################################################################

def main():


    users_age = int(input('How old are you? '))
    if users_age >= 18:
        print('Congrats! Go vote and make a difference! ')
    elif users_age < 18 and users_age > 0:
        years_left = 18 - users_age
        print(f'sorry, you have {years_left} years until you can vote.')
    else:
        print('issue was detected! ')

if __name__ == "__main__":
    main()











####################ASSIGNMENT PROMPT############################################################################


