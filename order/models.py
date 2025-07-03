from django.db import models
from user.models import *
from car.models import *

class OrderModel(models.Model):
    class OrderType(models.TextChoices):
        RESERVE = 'RS', '预定'
        FULL_PAYMENT = 'FP', '全款'
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    orderDate = models.DateField(auto_now_add=True)
    type = models.CharField(
        max_length=2,
        choices=OrderType.choices,
        default=OrderType.RESERVE
    )
    def __str__(self):
        return f"{self.orderDate} - {self.type}"
