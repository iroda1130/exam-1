from django.db import models


class Taxi(models.Model):
    taxi_name = models.CharField(max_length=100, null=False, blank=False)
    license = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    capacity = models.IntegerField()
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.taxi_name

