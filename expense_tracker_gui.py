import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QListWidget

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

        # Add a list widget to display the expenses
        self.expense_list = QListWidget(self)
        layout.addWidget(self.expense_list)

        central_widget.setLayout(layout)

        # Initialize an empty list to store expenses
        self.expenses = []

    def add_expense(self):
        # Get the text from the input filed
        expense_text = self.expense_input.text()

        # Display a message box if input is empty
        if not expense_text.strip():
            QMessageBox.warning(self, "Warning", "Expense description cannot be empty!")
        else:
            # Add the expense to the list
            self.expenses.append(expense_text)
            # Update the list widget to display the new expense
            self.update_expense_list()

            # Show a confirmation message
            QMessageBox.information(self, "Expense Added", f"Expense '{expense_text}' added successfully!")
            # Clear the input field
            self.expense_input.clear()
    
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
