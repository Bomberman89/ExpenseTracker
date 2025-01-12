import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox

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

        # Add a basic label
        welcome_label = QLabel("Welcome to the Expense Tracker!", self)
        welcome_label.setStyleSheet("font-size: 18px; margin: 20px;")
        layout.addWidget(welcome_label)

        # Add an input field for expenses
        self.expense_input = QLineEdit(self)
        self.expense_input.setPlaceholderText("Enter expense description")
        layout.addWidget(self.expense_input)

        # Add a button to submit expenses
        submit_button = QPushButton("Add Expense", self)
        submit_button.clicked.connect(self.add_expense)
        layout.addWidget(submit_button)

        central_widget.setLayout(layout)

    def add_expense(self):
        # Get the text from the input filed
        expense_text = self.expense_input.text()

        # Display a message box if input is empty
        if not expense_text.strip():
            QMessageBox.warning(self, "Warning", "Expense description cannot be empty!")
        else:
            # Show a confirmation message
            QMessageBox.information(self, "Expense Added", f"Expense '{expense_text}' added successfully!")
            # Clear the input field
            self.expense_input.clear()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTrackerGUI()
    window.show()
    sys.exit(app.exec())
