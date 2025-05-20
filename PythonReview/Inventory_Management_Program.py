################################################################################################
# Assignment: Implement your own Data Structures
# Name: Nicholas Hamilton
# This project is the eighth assignment in my GEN AI Externship with Cognizant.
# No AI is used in this project.
################################################################################################


def main():
    """
    simple Inventory Assignment for externship

    """
    print('welcome to inventory manager!')
    inventory = {}

    #print(help(inventory))

    try:
        print(inventory)
    except:
        print('cannot print inventory')



    inventory['mango'] = (30, 3.0)
    inventory['apple'] = (40, 1.0)
    inventory['banana'] = (100, 0.5)

    apple_present = inventory.__contains__('apple') # practicing here
    print(f' does the inventory contain an apple? {apple_present}')
    print('before removing banana \n')

    try:
        for key, value in inventory.items():
            print(f'key is {key}, value is {value}')
    except:
        (print('cannot print key value pairs'))

    inventory.pop('banana')
    print('after removing banana')
    try:
        for key, value in inventory.items():
            print(f'item is {key}, the quanity is {value[0]}, the cost is ${value[1]}')

    except:
        (print('cannot print key value pairs'))



if __name__ == "__main__":
    main()













