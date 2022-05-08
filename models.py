from tortoise import fields
from tortoise.models import Model


class Task(Model):
    id = fields.UUIDField(pk=True)
    property = fields.CharField(max_length=200)
    description = fields.CharField(max_length=200)
    date = fields.DatetimeField(auto_now_add=True)
    task_completed = fields.BooleanField(default=False)