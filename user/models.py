from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    balance = models.FloatField(default=0)
    def __str__(self):
        return f"{self.name} - {self.created_at} - {self.balance}"


