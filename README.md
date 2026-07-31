# Smart Expense Tracker API

## Overview

Smart Expense Tracker API is a RESTful web service built using FastAPI for managing personal expenses. The application allows users to create, retrieve, filter, summarize, and delete expense records. Expense data is stored in a local JSON file, providing a simple and lightweight persistence mechanism while meeting the assignment requirements.

---

## Features

- Create a new expense
- Retrieve all expenses
- Retrieve an expense by its ID
- Filter expenses by category
- View total expenses and category-wise summary
- Delete an expense
- Automatic request validation using Pydantic
- Interactive API documentation using Swagger UI and ReDoc
- Automated API testing using Pytest

---

## Technology Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- Pytest

---

## Project Structure

```text
expense-tracker-api/
│
├── data/
│   └── expenses.json
│
├── src/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── storage.py
│
├── tests/
│   └── test_api.py
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/anitapreety/expense-tracker-api.git
cd expense-tracker-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI development server:

```bash
uvicorn src.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## Bonus Feature

This project includes the optional **OpenAPI/Swagger Documentation** feature.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

These interfaces allow all API endpoints to be explored and tested directly from the browser.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home endpoint |
| POST | `/expenses/` | Create a new expense |
| GET | `/expenses/` | Retrieve all expenses |
| GET | `/expenses/{expense_id}` | Retrieve an expense by ID |
| GET | `/expenses/category/{category}` | Retrieve expenses by category |
| GET | `/expenses/summary` | Retrieve total and category-wise expense summary |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Running Tests

Run the automated test suite using:

```bash
python -m pytest
```

The tests verify the application's core functionality, including:

- Creating expenses
- Retrieving expenses
- Filtering expenses by category
- Viewing expense summaries
- Deleting expenses

---

## Design Decisions

The application was intentionally designed to remain simple, modular, and easy to maintain.

Key design decisions include:

- FastAPI was chosen for its simplicity, performance, and built-in API documentation.
- Pydantic models validate incoming request data before processing.
- JSON file storage was selected to satisfy the assignment requirements without introducing unnecessary complexity.
- The project is organized into separate modules for routing, models, and storage to improve readability and maintainability.
- Automated tests were added to verify the core API functionality.

---

## Future Improvements

Possible future enhancements include:

- Update existing expenses
- Database integration using SQLite or PostgreSQL
- Authentication and authorization
- Pagination for large datasets

---

## Author

Developed by **Anita Preety** as part of a Software Engineering Apprenticeship technical assessment using Python and FastAPI.