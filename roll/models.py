from django.db import models
from django.forms import ImageField


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'img/')
    description = models.TextField()

    def __str__(self):
        return self.name

