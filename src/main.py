from fastapi import FastAPI
from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="""
A lightweight REST API for managing personal expenses.

## Features
- Add a new expense
- View all expenses
- Filter expenses by category
- View expense summary
- Delete an expense
""",
    version="1.0.0"
)

app.include_router(router)


@app.get("/", tags=["Home"])
def root():
    """
    Welcome endpoint.
    """
    return {
        "message": "Welcome to Smart Expense Tracker API",
        "documentation": "/docs"
    }