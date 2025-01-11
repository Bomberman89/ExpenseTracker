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

def main():
    # This will hold our list of expenses
    expenses = []

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
            print("Add expense functionality goes here!")
        elif choice == "2":
            print("View expense functionality goes here!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()