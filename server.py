from uuid import UUID
from fastapi import FastAPI, HTTPException, Response
from database import create_start_app_handler
from models import Task
from typing import List
from schemas import TaskSchemaPublic, TaskCreate

def get_application():

    app = FastAPI()

    # connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))

    return app

app = get_application()



@app.post('/task-create', response_model=TaskSchemaPublic)
async def create_task(data: TaskCreate):
    if data:
        task = await Task.create(
            **data.dict(exclude_unset=True)
        )
        task.task_completed=False
        return task
    return HTTPException(status_code=400, detail="Check your task again!!")


@app.put('/task-get/{id}', response_model=List[TaskSchemaPublic])
async def update_task(id: str):
    get_task = Task.filter(id=id)
    if not get_task:
        return "Task object not Found"
    get_task.update(task_completed=True)
    return await get_task
    

@app.get('/task-list', response_model=List[TaskSchemaPublic])
async def list_task():
    return await Task.all()
