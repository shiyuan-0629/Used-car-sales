import re

from django.shortcuts import render, redirect
from django.urls import reverse
from favorites.models import *
from car.models import *
# Create your views here.
def favorites(request):
    userid = request.session.get('userid')
    favorite_records = FavoriteModel.objects.filter(user_id=userid)
    favorite_car_ids = [favorite.car_id for favorite in favorite_records]
    cars = CarModel.objects.filter(id__in=favorite_car_ids)
    return render(request,"favorite_info.html",{"cars":cars})

def remove(request,id):
    userid = request.session.get('userid')
    FavoriteModel.objects.filter(user_id=userid, car_id=id).delete()
    referer = request.META.get('HTTP_REFERER')
    if "favorites/favorites" in referer:
        return redirect(reverse('favorites:favorites'))
    else:
        return redirect(reverse('car:buy',kwargs={"id":id}))

def add(request,id):
    userid = request.session.get('userid')
    FavoriteModel.objects.create(user_id=userid, car_id=id)
    return redirect(reverse('car:buy',kwargs={'id':id}))