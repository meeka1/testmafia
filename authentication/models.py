from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username