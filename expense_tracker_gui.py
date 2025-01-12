import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class ExpenseTrackerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Add a basic label
        layout = QVBoxLayout()
        welcome_label = QLabel("Welcome to the Expense Tracker!", self)
        welcome_label.setStyleSheet("font-size: 18px; margin: 20px;")
        layout.addWidget(welcome_label)

        central_widget.setLayout(layout)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTrackerGUI()
    window.show()
    sys.exit(app.exec())
