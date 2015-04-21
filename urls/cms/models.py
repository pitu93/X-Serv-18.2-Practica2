from django.db import models

# Create your models here.

class Url(models.Model):
    original = models.CharField(max_length=32)
