import csv
import shutil

def save_expenses_to_file(expenses, filename="expenses.csv"):
    """
    Saves the list of expenses to a CSV file.

    Args:
        expenses (list): List of expense strings to save.
        filename (str): Name of the file to save the expenses to.
    """
    # Create a backup of the existing file before overwriting it
    backup_filename = filename + ".bak"
    try:
        shutil.copy(filename, backup_filename)
    except FileNotFoundError:
        # No backup is created if the file doesn't exist
        pass

    # Save the updated expenses to the file
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense])

def load_expenses_from_file(filename="expenses.csv"):
    """
    Loads expenses from a CSV file.
    
    Args:
        filename (str): Name of the file to load the expenses from.
    
    Returns:
        list: A list of expense strings.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []