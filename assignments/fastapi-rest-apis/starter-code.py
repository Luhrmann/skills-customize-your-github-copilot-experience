from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="Tasks API - FastAPI Starter", version="1.0")


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: str


# In-memory storage (list of dicts)
tasks: List[dict] = []


@app.get("/tasks", response_model=List[Task], summary="List tasks")
def list_tasks(skip: int = 0, limit: int = 100):
    return tasks[skip : skip + limit]


@app.get("/tasks/{task_id}", response_model=Task, summary="Get a single task")
def get_task(task_id: str):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):
    new_task = Task(id=str(uuid4()), **task.dict())
    tasks.append(new_task.dict())
    return new_task


@app.put("/tasks/{task_id}", response_model=Task, summary="Update an existing task")
def update_task(task_id: str, task: TaskCreate):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            updated = Task(id=task_id, **task.dict())
            tasks[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: str):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")


# Optional sample data
if not tasks:
    tasks.append(
        Task(id=str(uuid4()), title="Example task", description="This is an example", done=False).dict()
    )
