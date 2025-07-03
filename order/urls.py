from django.urls import path
from order.views import *
urlpatterns = [
    path('order/',order,name='order'),
    path('reserve/<int:id>/',reserve,name='reserve'),
    path('buy/<int:id>/',buy,name='buy'),
]