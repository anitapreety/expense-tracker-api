# Smart Expense Tracker API

## Overview

Smart Expense Tracker API is a RESTful web service built using FastAPI for managing personal expenses. It allows users to create, retrieve, filter, summarize, and delete expense records. Expense data is stored in a local JSON file, providing a simple and lightweight persistence mechanism while meeting the assignment requirements.

---

# Features

- Add a new expense
- Retrieve all expenses
- Retrieve an expense by its ID
- Filter expenses by category
- View expense summary (total expenses and category-wise totals)
- Delete an expense
- Automatic request validation using Pydantic
- Interactive OpenAPI documentation with Swagger UI and ReDoc
- Automated API testing using Pytest

---

# Technology Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- Pytest

---

# Project Structure

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

# Installation

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/expense-tracker-api.git
```

Navigate to the project folder:

```bash
cd expense-tracker-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install all required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI development server:

```bash
uvicorn src.main:app --reload
```

The application will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation (Bonus Feature)

FastAPI automatically generates interactive OpenAPI documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

This project uses FastAPI's built-in OpenAPI documentation as the optional bonus feature.

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home endpoint |
| POST | `/expenses/` | Create a new expense |
| GET | `/expenses/` | Retrieve all expenses |
| GET | `/expenses/{expense_id}` | Retrieve an expense by ID |
| GET | `/expenses/category/{category}` | Retrieve expenses by category |
| GET | `/expenses/summary` | Retrieve expense summary |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

# Running Tests

Run the automated test suite using:

```bash
python -m pytest
```

The test suite verifies the core API functionality including:

- Creating an expense
- Retrieving expenses
- Retrieving expenses by category
- Viewing expense summary
- Deleting an expense

---

# Design Decisions

The project was intentionally kept simple and modular.

Key design decisions include:

- FastAPI was chosen for its performance, simplicity, and automatic API documentation.
- Pydantic models are used to validate incoming request data.
- JSON file storage was selected because it satisfies the assignment requirements without introducing unnecessary complexity.
- The application is separated into modules for routing, models, and storage to improve maintainability.
- Automated tests were added to verify the application's core functionality.

---

# Future Improvements

Possible future enhancements include:

- Update existing expenses
- Database integration using SQLite or PostgreSQL
- Authentication and authorization
- Pagination for large datasets

---

# Author

Developed by **Anita Preety** as part of a Software Engineering Apprenticeship technical assessment using Python and FastAPI.