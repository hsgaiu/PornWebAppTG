from tortoise import fields
from tortoise.models import Model

class modelUser(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100)

    class Meta:
        table = "users"