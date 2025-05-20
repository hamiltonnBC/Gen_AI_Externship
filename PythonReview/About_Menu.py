
################################################################################################
# Assignment: About Menu
# Name: Nicholas Hamilton
# This project is the tenth assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################
import turtle





def factorial_func(n):

    if n == 1:
        return n



    return n * factorial_func(n - 1)


def fib_func(n):

    if n <= 1:
        return n

    return fib_func(n - 1) + fib_func(n - 2)


def draw_design(t,n):

    if n == 0:
        return

    t.forward(50)
    t.left(n)

    draw_design(t, n-1)

def main():
    """
    simple recursion practice

    """

    # Menu of Recursion Functions



    user_is_playing = True

    while user_is_playing:
        while True:
            user_choice = int(input('what would you like to do? Please enter just a number as response.\n '
                                    '1 Calculate factorial of a number\n'
                                    '2 Find the nth Fibonacci number\n'
                                    '3 Draw a recursive fractal pattern\n'
                                    '4 Exit'))

            if user_choice not in {1, 2, 3, 4}:
                print('invalid entry, try again!')
            else:
                break

        if user_choice == 1:
            user_num = int(input('what number would you like to find the factorial of?'))
            print(f' the factorial of {user_num} is {factorial_func(user_num)}')

        if user_choice == 2:
            user_num = int(input('what number would you like to find the fib of?'))
            print(f' fib {fib_func(user_num)}')

        if user_choice == 3:
            t = turtle.Turtle()
            t.speed(0)
            wn = turtle.Screen()
            t.color('blue')

            draw_design(t,n=200)
            wn.exitonclick()


        if user_choice == 4:
            user_is_playing = False


    print('thanks for playing!')

if __name__ == "__main__":
    main()













