from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from models import TaskCreate, TaskUpdate, Task
from database import get_db_connection, create_table

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield


app= FastAPI(lifespan=lifespan)


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    with get_db_connection() as connection:
        cursor = connection.execute("""
        INSERT INTO tasks (title, description, completed)
        VALUES (?, ?, ?)
        """,
        (task.title, task.description, int(task.completed))
        )

        task_id = cursor.lastrowid

    return Task(id=task_id, **task.model_dump())



@app.get("/tasks", response_model=list[Task])
def get_tasks():
    with get_db_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM tasks"
        ).fetchall()

    return [Task(**dict(row)) for row in rows]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id:int):
    with get_db_connection() as connection:
        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404, 
            detail="Task not found"
            )
    return Task(**dict(row))


@app.put("/tasks/{task_id}", response_model=Task)
def replace_task(task_id:int, task: TaskCreate):
    with get_db_connection() as connection:
        cursor = connection.execute(
            """UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?""",
            (task.title,
             task.description,
             int(task.completed),
             task_id)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")

    return Task(id=task_id, **task.model_dump())



@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id:int, task: TaskUpdate):
    changes = task.model_dump(exclude_unset=True)

    if "title" in changes and changes ["title"] is None:
        raise HTTPException(
            status_code=422, 
            detail="Title cannot be null"
            )
    with get_db_connection() as connection:
            row = connection.execute(
                "SELECT *FROM tasks WHERE id = ?",
                (task_id,)
            ).fetchone()

            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Task not found"
                )
            current_task = Task(**dict(row))
            updated_task = current_task.model_copy(update=changes)

            connection.execute(
                """UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?""",
                (
                    updated_task.title,
                    updated_task.description,
                    int(updated_task.completed),
                    task_id
                )
            )
    return updated_task


    

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id:int):
    with get_db_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM tasks WHERE id =?",
            (task_id,)
        )
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
    return None



