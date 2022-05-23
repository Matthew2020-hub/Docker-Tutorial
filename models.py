from tortoise import fields
from tortoise.models import Model


class Register(Model):
    id = fields.UUIDField(pk=True)
    full_name = fields.CharField(max_length=200)
    password = fields.CharField(max_length=50)

