from django.db import models

class Task(models.Model):
    task=models.CharField(max_length=50)
    priority=models.IntegerField()
    date=models.DateField()
    