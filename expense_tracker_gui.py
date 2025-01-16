import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QListWidget
import expense_manager # Import the shared module
import shutil
# Backup the file as soon as the program starts
try:
    shutil.copy("expenses.csv", "expenses_initial.bak")
except FileNotFoundError:
    # If the file doesn't exist yet, no backup is created
    pass

class ExpenseTrackerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout for the central widget
        layout = QVBoxLayout()

        # Add a welcome label
        welcome_label = QLabel("Welcome to the Expense Tracker!", self)
        welcome_label.setStyleSheet("font-size: 25px; margin: 20px;")
        layout.addWidget(welcome_label)

        # Add an input field for expenses
        self.expense_input = QLineEdit(self)
        self.expense_input.setPlaceholderText("Enter expense description")
        layout.addWidget(self.expense_input)

        # Add a button to submit expenses
        submit_button = QPushButton("Add Expense", self)
        submit_button.clicked.connect(self.add_expense)
        layout.addWidget(submit_button)

        # Add a button to delete selected expenses
        delete_button = QPushButton("Delete Selected Expense", self)
        delete_button.clicked.connect(self.delete_selected_expense)
        layout.addWidget(delete_button)

        # Add a list widget to display the expenses
        self.expense_list = QListWidget(self)
        layout.addWidget(self.expense_list)

        central_widget.setLayout(layout)

        # Load expenses from the file on startup
        self.expenses = expense_manager.load_expenses_from_file()
        self.update_expense_list()

    def add_expense(self):
        # Get the text from the input filed
        expense = self.expense_input.text().strip()

        # Display a message box if input is empty
        if not expense:
            QMessageBox.warning(self, "Invalid Input", "Expense cannot be empty!")
            return
        # Add the expense to the list
        self.expenses.append(expense)
        # Update the list widget to display the new expense
        self.update_expense_list()

        # Save expenses to file
        expense_manager.save_expenses_to_file(self.expenses)

        # Clear the input field
        self.expense_input.clear()

        # Show a confirmation message
        QMessageBox.information(self, "Success", "Expense added successfully!")
        
    def delete_selected_expense(self):
        # Get the currently selected item
        selected_item = self.expense_list.currentItem()

        if selected_item:
            # Remove the selected item from the expense list
            selected_expense = selected_item.text()
            self.expenses.remove(selected_expense)
            self.update_expense_list()

            # Save the updated list to the file
            expense_manager.save_expenses_to_file(self.expenses)

            QMessageBox.information(self, "Expense Deleted", f"Expense '{selected_expense}' deleted successfully!")
        else:
            QMessageBox.warning(self, "Warning", "Please select an expense to delete!")

    def update_expense_list(self):
        # Clear the existing list and add the updated expenses
        self.expense_list.clear()
        self.expense_list.addItems(self.expenses)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTrackerGUI()
    window.show()
    sys.exit(app.exec())
