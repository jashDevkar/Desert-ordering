from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=20)
    major = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    