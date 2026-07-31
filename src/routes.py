from fastapi import APIRouter, status, HTTPException
from src.models import Expense, ExpenseResponse, SummaryResponse
from src.storage import load_expenses, save_expenses, get_next_id

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new expense"
)
def add_expense(expense: Expense):
    """
    Add a new expense to the expense tracker.
    """
    expenses = load_expenses()

    new_expense = {
        "id": get_next_id(expenses),
        **expense.model_dump()
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense


@router.get(
    "/",
    response_model=list[ExpenseResponse],
    summary="Get all expenses"
)
def get_expenses():
    """
    Retrieve all saved expenses.
    """
    return load_expenses()


@router.get(
    "/category/{category}",
    response_model=list[ExpenseResponse],
    summary="Filter expenses by category"
)
def get_expenses_by_category(category: str):
    """
    Retrieve all expenses belonging to a specific category.
    """
    expenses = load_expenses()

    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


@router.get(
    "/summary",
    response_model=SummaryResponse,
    summary="Get expense summary"
)
def get_summary():
    """
    Returns the total expenses and category-wise expense summary.
    """
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    by_category = {}

    for expense in expenses:
        category = expense["category"]
        by_category[category] = by_category.get(category, 0) + expense["amount"]

    return {
        "total_expenses": total,
        "by_category": by_category
    }


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    summary="Get expense by ID"
)
def get_expense(expense_id: int):
    """
    Retrieve a single expense by its ID.
    """
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )


@router.delete(
    "/{expense_id}",
    summary="Delete expense"
)
def delete_expense(expense_id: int):
    """
    Delete an expense using its ID.
    """
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )