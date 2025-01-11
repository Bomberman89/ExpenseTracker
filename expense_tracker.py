def main():
    # Runs loop that keeps displaying the menu options until the user chooses the exit (option 3)
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        # Based on user input, it will call the appropriate function
        if choice == "1":
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