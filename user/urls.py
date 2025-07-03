from django.urls import path
from user.views import *
urlpatterns = [
    path('info/', info, name='info'),
    path('accountInfo/', accountInfo, name='accountInfo'),
    path('favoriteInfo/', favoriteInfo, name='favoriteInfo'),
    path('orderInfo/', orderInfo, name='orderInfo'),
    path('loginInfo/', loginInfo, name='loginInfo'),

]