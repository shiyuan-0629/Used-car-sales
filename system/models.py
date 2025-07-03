from django.db import models

from user.models import UserModel


# Create your models here.
class SystemModel(models.Model):
    class SystemType(models.TextChoices):
        login = 'login', '登录'
        logout = 'logout', '登出'

    class SystemState(models.TextChoices):
        success = 'success', '成功'
        fail = 'fail', '失败'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=8,
        choices=SystemState.choices,
        default=SystemState.success
    )
    type = models.CharField(
        max_length=8,
        choices=SystemType.choices,
        default=SystemType.login
    )
    lastDate = models.DateField(auto_now_add=True)
