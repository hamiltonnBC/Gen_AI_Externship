################################################################################################
# Assignment: AI Powered-Text-Completion
# Name: Nicholas Hamilton
# This project is the Capstone in my GEN AI Externship with Cognizant.
# This app uses OpenAI's GPT model for text generation.
################################################################################################


def menu():
    available_options = {1, 2, 3, 4}

    while True:
        try:
            users_desired_action = int(input('What would you like to do? \n'
                                             '1. Add Expense\n'
                                             '2. View All Expenses\n'
                                             '3. View Summary\n'
                                             '4. Exit\n'
                                             'Please answer a simple 1, 2, 3, or 4 \n'))
        except ValueError:
            print('this was not a number, please try again!\n\n')
            continue
        if users_desired_action not in available_options:
            print('please enter 1, 2, 3, or 4. ')
            continue
        else:
            return users_desired_action


def add_category():
    return input('Please enter the name of your new category: \n')


def add_expense(list_of_existing_categories: list, data: dict) -> dict:
    """
    Adds an expense to the data dictionary.
    Users provide a description (str), a category (str), and an amount (float).
    Data is stored as: {category: [(amount, description), ... etc]}
    """
    while True:
        try:
            is_new_category_needed = int(input(
                "Do you need a new category for this expense, or will you be using an existing one?\n1 for new, 2 for existing category.\n"))
            if is_new_category_needed == 1:
                new_category = add_category()
                list_of_existing_categories.append(new_category)
                print(f'Added new category: {new_category}')
            elif is_new_category_needed == 2:
                print('Using existing category.\n')
            else:
                print('Invalid input. Please enter 1 or 2.')
                continue
        except ValueError:
            print('Invalid input. Please enter 1 or 2.')
            continue

        category_selection = input(f'Select a category (exactly as shown): {list_of_existing_categories}\n')
        if category_selection not in list_of_existing_categories:
            print('Category not found. please try again!\n')
            continue

        try:
            entry_description = input('Enter the expense description (e.g., Lunch for Food):\n')
            entry_expense = float(input('Enter the expense amount:\n'))
        except ValueError:
            print('Amount must be a number. Please Try again.\n')
            continue

        new_entry = (entry_expense, entry_description)
        if category_selection not in data:
            data[category_selection] = []
        data[category_selection].append(new_entry)

        return data


def view_expenses(data):
    """
    Displays all expenses in the data dictionary.
    """
    if not data:  # in the case that it is currently empty
        print("No expenses found.")
        return

    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for expense in expenses:
            print(f" The amount: {expense[0]}, The description: {expense[1]}")


def view_summary(data):
    """shows the total amount spent per category.
    """
    if not data:  # in the case that it is currently empty
        print("No expenses found.")
        return

    summary = {}
    for category, expenses in data.items():
        total = sum(expense[0] for expense in expenses)
        summary[category] = total

    print("\nSummary of Expenses by Category:")
    for category, total in summary.items():
        print(f"Category: {category}, Total Amount Spent: {total}")


def main():
    """
    Main function to run the Personal Finance Tracker.
    :return:
    """
    print('Welcome to the Personal Finance Tracker!')
    list_of_existing_categories = ['food', 'housing', 'entertainment']
    data = {}

    while True:
        users_desired_action = menu()

        if users_desired_action == 1:
            add_expense(list_of_existing_categories, data)
        elif users_desired_action == 2:
            view_expenses(data)
        elif users_desired_action == 3:
            view_summary(data)
        elif users_desired_action == 4:
            print("Exiting program.")
            break

    print('Thank you so much for playing!')


if __name__ == "__main__":
    main()

## ASSIGNMENT PROMPT ######################

# You will build a command-line Python program that allows users to:
#
# Add an expense with a description, category, and amount.
#
# View all expenses.
#
# View a summary of expenses by category.
#
# Handle invalid inputs gracefully using exception handling.
#
# Store data in a dictionary (category as key, list of tuples as values).
#
# This program simulates a real-world task and tests your ability to organize code into functions and use various Python data structures effectively.











