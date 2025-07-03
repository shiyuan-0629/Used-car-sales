from django.urls import path
from notice.views import *
urlpatterns = [
    path('', notice, name='notice'),
]