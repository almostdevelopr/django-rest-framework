from django.db import models

# Create your models here.


class Person(models.Model):
    """A simple representation of a person."""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
