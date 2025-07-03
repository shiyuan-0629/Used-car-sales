from django.urls import path,include
from favorites.views import *
urlpatterns = [
    path('favorites/',favorites,name='favorites'),
    path('remove/<int:id>',remove,name='remove'),
    path('add/<int:id>',add,name='add'),
]
