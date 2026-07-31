# AI Usage Notes

## Overview

AI was used as a development assistant throughout this project to help me understand concepts, review implementation ideas, and debug issues. I did not rely on AI output without verification. Every feature included in the final submission was manually reviewed, tested, and validated before being accepted.

---

## 1. Which parts were AI-assisted and which parts were implemented by me?

### AI-Assisted

AI was mainly used to:

- Explain FastAPI concepts and recommended project structure.
- Suggest how to organize the application into separate modules (`main.py`, `routes.py`, `models.py`, and `storage.py`).
- Explain Pydantic request validation.
- Help understand error messages during development.
- Review the overall code structure for readability and maintainability.
- Suggest improvements to the README and project documentation.

### Implemented and Verified by Me

I implemented the project feature by feature and integrated the suggestions into the application.

My work included:

- Implementing the API endpoints.
- Integrating JSON-based data storage.
- Connecting the routes with the storage layer.
- Running and testing every endpoint.
- Writing and executing automated tests.
- Reviewing the final project before submission.

Although AI assisted during development, I manually verified every feature before including it in the final project.

---

## 2. What did I validate, test, or change?

I validated all AI-assisted changes before accepting them.

My validation process included:

- Running the application locally using Uvicorn.
- Testing every endpoint using FastAPI Swagger UI.
- Verifying that expense data was correctly stored and retrieved from the JSON file.
- Running automated tests using Pytest until all tests passed successfully.
- Reviewing the project structure to ensure it remained clean and modular.

### Example

During development, I encountered the following error:

```
TypeError: Object of type date is not JSON serializable
```

AI explained why Python's JSON module could not directly serialize `date` objects. After understanding the root cause, I updated the storage implementation, tested the API again, and confirmed that the issue had been resolved.

This process helped me better understand JSON serialization rather than simply applying a suggested fix.

---

## 3. AI Suggestions I Decided Not to Use

During development, AI suggested additional enhancements such as introducing a database, adding more advanced features, and increasing the overall project complexity.

I chose not to implement those suggestions because the assignment specifically required JSON-based persistence. Keeping the project focused on the stated requirements made the implementation simpler, easier to understand, and more aligned with the assessment expectations.

I also avoided adding unnecessary frameworks or features that were not required for the assignment.

---

## Reflection

This project improved my understanding of FastAPI, REST API development, request validation using Pydantic, JSON-based persistence, debugging, and automated testing.

AI served as a learning and development assistant throughout the project, while the implementation, testing, validation, and final review were completed manually before submission.