################################################################################################
# Assignment: Hands on Python Data Structures
# Name: Nicholas Hamilton
# This project is the seventh assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################


def list_practice():

    fruits = ['apple', 'mango', 'banana', 'pear']

    print(f' original fruits are {fruits}')

    fruits.append('grapefruit')
    print(f' after appending grapefruit, fruits are {fruits}')

    fruits.remove('banana')
    print(f' after removing banana, fruits are {fruits}')

    reverse_fruits = fruits[::-1]
    print(f' after reversing the list, fruits are {reverse_fruits}')


def dictionary_practice():

    me = {'my_name': 'nicholas', 'age': '100', 'city': 'Washington DC'}
    print(me.get('my_name', 'not found!'))

    me['city'] = 'NYC'

    print(f' after changing city, my dictionary is {me}')

    for key, value in me.items():
        print(f'key: {key}, value: {value}')
    print(f' my name is {me.get("my_name", "not found!")}, I am {me.get("age", "not found!")}, '
          f'and I live in {me.get("city", "not found!")}')



def tuple_practice():

    my_items = ('The Lion King', 'Twinkle Twinkle Little Star', 'War and Peace')

    try:
        my_items.append('attempt')
    except:
        print('these are immutable')
        print(f'Length of tuple is {len(my_items)}')



def set_practice(): # Just for practice, not apart of assignment

    hobbies = {'rock climbing', 'swimming', 'eating'} # doing hobbies for my set
    hobbies.add('cycling')
    print(f' hobbies include {hobbies}')

    try:
        hobbies.remove('cycling')
    except:
        print('cannot remove')

def main():
    """
    simple Data Structure Practice

    """

    list_practice()

    dictionary_practice()

    tuple_practice()

    set_practice()


if __name__ == "__main__":
    main()













