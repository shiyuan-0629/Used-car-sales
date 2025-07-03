
from django.shortcuts import render

from car.models import CarModel
from order.models import OrderModel
from datetime import date

# Create your views here.
def order(request):
    userid = request.session.get('userid')
    orders = OrderModel.objects.filter(user=userid).order_by('-orderDate')
    datas = []
    for order in orders:
        data = {'id': order.id,
                'car_id': order.car_id,
                'car_name': CarModel.objects.get(id=order.car_id).name,
                'orderDate': order.orderDate,
                'type': order.type}
        datas.append(data)
    return render(request,"order_info.html",{"orders":datas})

def reserve(request,id):
    userid = request.session.get('userid')
    OrderModel.objects.create(car_id=id,user_id=userid,type='RS',orderDate=date.today())
    return render(request,"info.html",{"default":"user:orderInfo"})

def buy(request,id):
    userid = request.session.get('userid')
    OrderModel.objects.create(car_id=id, user_id=userid, type='FP', orderDate=date.today())
    return render(request, "info.html", {"default": "user:orderInfo"})
