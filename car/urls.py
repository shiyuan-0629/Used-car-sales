from django.urls import path
from car.views import *
urlpatterns = [
    path('cars/',index, name='cars'),
    path('buy/<int:id>/',buy, name='buy'),
]