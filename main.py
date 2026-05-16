from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str

# In-memory task storage for simplicity
tasks = [
    Task(id=1, title="Task 1", description="This is task 1"),
    Task(id=2, title="Task 2", description="This is task 2"),
]

# Create endpoint
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

# Read endpoint
@app.get("/tasks")
def read_tasks():
    return tasks

# Update endpoint
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for t in tasks:
        if t.id == task_id:
            t.title = task.title
            t.description = task.description
            return t
    return {"error": "Task not found"}

# Delete endpoint
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}