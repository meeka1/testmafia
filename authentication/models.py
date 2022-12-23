from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=200,blank=False)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username