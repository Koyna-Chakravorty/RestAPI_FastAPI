## Task Management REST API

A RESTful API built using Python and FAstAPI that allows users to create, retrieve, update, and delete tasks.

The project demonstrates backend API development, data validation, SQLite database integration, and HTTP error handling.

## Technologies Used
- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Swagger UI/ ReDoc

## Features
- Create new tasks
- Retrieve all tasks or individual tasks
- Replace existing task information
- Partially update task information
- Delete tasks
- Validate incoming data using Pydantic
- Store tasks persistently using SQLite
- Handle invalid requests and missing tasks
- Automatically generated API documentation

## API Endpoints

- **POST `/tasks`** — Create a new task
- **GET `/tasks`** — Retrieve all tasks
- **GET `/tasks/{task_id}`** — Retrieve a specific task
- **PUT `/tasks/{task_id}`** — Replace an existing task
- **PATCH `/tasks/{task_id}`** — Partially update a task
- **DELETE `/tasks/{task_id}`** — Delete a task

## Installation and Setup

1. Clone the repository

```bash
git clone https://github.com/Koyna-Chakravorty/RestAPI_FastAPI.git
cd RestAPI_FastAPI
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the environment

On Windows PowerShell:
```bash
.\.venv\Scripts\Activate.ps1
```

On macOS/ Linux:
```bash
source .venv/bin/activate
```

4. Install dependencies
```bash
python -m pip install -r requirements.txt
```

5. Run the API
```bash
python -m uvicorn main:app --reload
```

6. Access API documentation

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

## Example Request

create a new task using POST /tasks:
```bash
{
  "title": "Complete FastAPI project",
  "description": "Build and test REST endpoints",
  "completed": false
}
```

Example response:
```bash
{
  "id": 1,
  "title": "Complete FastAPI project",
  "description": "Build and test REST endpoints",
  "completed": false
}
```

## Database

the API uses SQLite for persistent task storage.
The database and task are created automatically when the application starts.
Local databse files are excluded from version control.

## Future Improvements

- User authentication
- Task filtering and searching
- Automated tests with pytest
- Pagination
- Frontend integration


## Project Status

Core API implementation complete.