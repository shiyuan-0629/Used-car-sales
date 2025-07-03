from django.db import models

from order.models import *

# Create your models here.
class MessageModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    message = models.TextField()
    messageDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.message