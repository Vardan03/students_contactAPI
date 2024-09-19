from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contacts = models.JSONField()
    createdAt = models.DateTimeField(auto_now_add=True)  # Устанавливается при создании
    updatedAt = models.DateTimeField(auto_now=True)  # Обновляется при каждом сохранении

