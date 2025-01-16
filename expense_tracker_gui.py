import sys
import shutil
import csv
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, 
    QListWidget, QLineEdit, QWidget, QMessageBox, QLabel
)

import expense_manager # Import the shared module

class ExpenseTrackerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.expenses = expense_manager.load_expenses_from_file()

        # Backup the file as soon as the program starts
        try:
            shutil.copy("expenses.csv", "expenses_initial.bak")
        except FileNotFoundError:
            # If the file doesn't exist yet, no backup is created
            pass

        # Set window title and size
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()

    def init_ui(self):
        # Layout for the central widget
        layout = QVBoxLayout()

        # Add a welcome label
        welcome_label = QLabel("Welcome to the Expense Tracker!", self)
        welcome_label.setStyleSheet("font-size: 25px; margin: 20px;")
        layout.addWidget(welcome_label)

        # Expense List
        self.expense_list = QListWidget()
        self.update_expense_list()
        layout.addWidget(self.expense_list)

        # Input and Buttons
        input_layout = QHBoxLayout()
        self.expense_input = QLineEdit()
        self.expense_input.setPlaceholderText("Enter an expense")
        input_layout.addWidget(self.expense_input)

        add_button = QPushButton("Add Expense")
        add_button.clicked.connect(self.add_expense)
        input_layout.addWidget(add_button)

        delete_button = QPushButton("Delete Selected Expense")
        delete_button.clicked.connect(self.delete_selected_expense)
        input_layout.addWidget(delete_button)

        layout.addLayout(input_layout)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def update_expense_list(self):
        # Clear the existing list and add the updated expenses
        self.expense_list.clear()
        self.expense_list.addItems(self.expenses)
    
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
            expense = selected_item.text()
            self.expenses.remove(expense)
            self.update_expense_list()
            # Save the updated list to the file
            expense_manager.save_expenses_to_file(self.expenses)
            QMessageBox.information(self, "Success", "Expense deleted successfully!")
        else:
            QMessageBox.warning(self, "No Selection", "Please select an expense to delete.")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTrackerGUI()
    window.show()
    sys.exit(app.exec())
