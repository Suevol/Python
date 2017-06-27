from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=32)
    mail = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    text = models.CharField(max_length=200)