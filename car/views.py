from django.shortcuts import render

# from car.models import *
from favorites.models import *
from message.models import *
from user.models import *

# Create your views here.
def index(request):
    search = request.GET.get('search', "")
    cars = CarModel.objects.filter(name__icontains=search)
    return render(request, "cars.html", {"cars":cars})

def buy(request,id):
    car = CarModel.objects.get(id=id)
    userid = request.session.get('userid')
    favorite = FavoriteModel.objects.filter(user_id=userid,car_id=id)
    messages = MessageModel.objects.filter(car_id=id).order_by('-messageDate')
    messages_by_user = {}
    for message in messages:
        user = UserModel.objects.get(id=message.user_id)
        if user.name not in messages_by_user:
            messages_by_user[user.name] = []
        messages_by_user[user.name].append(message.message)
    if favorite.exists():
        return render(request, "car.html", {"car": car, "tip":"取消收藏","message":messages_by_user})
    else:
        return render(request, "car.html", {"car":car,"tip":"收藏","message":messages_by_user})
