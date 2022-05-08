from email.policy import default
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TaskSchemaPublic(BaseModel):
    id: UUID
    description: str
    property: str
    date: datetime
    task_completed: Optional[bool] = False


class TaskCreate(BaseModel):
    description: str
    property: str
    task_completed: Optional[bool] = False
