from django.urls import path
from message.views import *
urlpatterns = [
    path('add/',add, name='add'),
]