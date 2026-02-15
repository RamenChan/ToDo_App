from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from .producer import publish_message

app = FastAPI(title="Platform Solutions Team FastAPI + RabbitMQ Example")


class Task(BaseModel):
    title: str
    description: str | None = None


@app.post("/tasks")
async def create_task(task: Task, background: BackgroundTasks):
    background.add_task(publish_message, task.dict())
    return {"status": "queued", "task": task}


@app.get("/")
async def root():
    return {"msg": "Platform Solutions Team FastAPI + RabbitMQ example. POST /tasks to enqueue."}
