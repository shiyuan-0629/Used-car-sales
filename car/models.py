from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    picture = models.CharField(max_length=200)

    def __str__(self):
        return self.name