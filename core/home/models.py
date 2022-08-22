from django.db import models

# Create your models here.


class Color(models.Model):
    """A simple representation of a color."""
    color_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.color_name


class Person(models.Model):
    """A simple representation of a person."""
    color = models.ForeignKey(
        Color, null=True, blank=True, on_delete=models.CASCADE, related_name="color")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
