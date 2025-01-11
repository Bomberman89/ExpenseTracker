# Import the json package
import json

# Attempts to load expenses from a JSON file
def load_expenses(filename):
    try:
        # Open file with "r" read-only capabilites
        with open(filename, "r") as file:
            expenses = json.load(file)
    # Returns empty list if file is not found
    except FileNotFoundError:
        expenses = []
    return expenses

# Saves the current list of expenses to the JSON file
def save_expenses(filename, expenses):
    # Open file with "w" read and write capabilities
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

# Prompts the user to enter the details for an expense
def add_expense(expenses):
    print("\nEnter Expense Details:")
    name = input("Enter Name: ")
    amount = float(input("Amount: $"))
    date = input("Date (YYYY-MM-DD): ")

    # Create a dictionary to represent the expense
    expense = {
        "name": name,
        "amount": amount,
        "date": date
    }

    # Add the expense to the list
    expenses.append(expense)

    print("\nExpense added successfully!")

# Show user the expenses if there are any
def view_expenses(expenses):
    # Check for expenses
    if not expenses:
        print("\nNo expenses added yet.")
    else:
        print("\nExpenses:")
        # Loop through the expenses list and print each in a readable format
        for expense in expenses:
            print(f"{expense['date']} - {expense['name']}: ${expense['amount']:.2f}")

def main():
    # This will be the name of our file for now
    filename = "expenses.json" ## Would like to add functionality for user to decide between custom or default names
    # Load the expenses from file at the start
    expenses = load_expenses(filename)

    # Runs loop that keeps displaying the menu options until the user chooses the exit (option 3)
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        # Based on user input, it will call the appropriate function
        if choice == "1":
            # Call the function to add an expense
            add_expense(expenses)
            # Save expenses to the file after adding
            save_expenses(filename, expenses)
        elif choice == "2":
            # Call the function to view expenses
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            # Save expenses to the file when exiting
            save_expenses(filename, expenses)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
