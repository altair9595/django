from django.db import models

# Create your models here.

class post(models.Model):
    titel = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
