# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful API using the FastAPI framework. You will design endpoints, validate input with Pydantic models, and run the app with Uvicorn.

## 📝 Tasks

### 🛠️ Task 1 — Basic CRUD API

#### Description
Create a FastAPI application that manages a list of "tasks" (to-do items).

#### Requirements
- Implement endpoints:
  - `GET /tasks` — list tasks (support `skip` and `limit` query params)
  - `GET /tasks/{id}` — retrieve a single task
  - `POST /tasks` — create a new task
  - `PUT /tasks/{id}` — update a task
  - `DELETE /tasks/{id}` — delete a task
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes and error messages

### 🛠️ Task 2 — Validation & Docs

#### Description
Add validation and ensure automatic docs work.

#### Requirements
- Use Pydantic `BaseModel` to validate input
- Add helpful `summary`/`description` where appropriate
- Verify OpenAPI docs at `/docs` and `/redoc`

### 🛠️ Task 3 — (Optional) Persistence

#### Description
Persist data between restarts.

#### Requirements
- (Optional) Add SQLite persistence (e.g., `sqlite3`, `SQLModel`, or `SQLAlchemy`)
- Explain any additional setup in this README

## 📦 Starter code

See `starter-code.py` for a minimal FastAPI app you can extend.

## ▶️ Run instructions

1. Create and activate a virtual environment (Windows):
   - `python -m venv venv`
   - `venv\Scripts\activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run the server:
   - `uvicorn starter-code:app --reload --port 8000`
4. Open the API docs:
   - `http://127.0.0.1:8000/docs`

## ✅ Deliverables

- `starter-code.py` — your completed API
- A short note in this README describing any extra features or choices

## 💡 Hints

- Start with in-memory storage (a Python list) before adding a database
- Use `uuid4()` for simple IDs
- Use `response_model` in route decorators for consistent responses
