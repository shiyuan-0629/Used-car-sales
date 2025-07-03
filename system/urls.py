from django.urls import path
from system.views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('loginlist/',loginlist,name='loginlist'),
    path('logout/',logout,name='logout'),
    path('updatepwd/',updatepwd,name='updatepwd'),
]