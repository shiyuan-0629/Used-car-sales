from user.models import *
from car.models import *
from django.db import models

# Create your models here.

class FavoriteModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)