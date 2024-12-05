from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredient = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)

    def __str__(self):
        return self.name
