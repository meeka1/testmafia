import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=200,blank=False)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username