import json
from pathlib import Path

DATA_FILE = Path("data/expenses.json")


def load_expenses():
    """
    Load all expenses from the JSON file.
    """
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    """
    Save all expenses to the JSON file.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, default=str)


def get_next_id(expenses):
    """
    Generate the next expense ID.
    """
    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1