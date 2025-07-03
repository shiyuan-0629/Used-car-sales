from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse

from message.models import MessageModel



# Create your views here.

def add(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        reviewContent = request.POST.get('reviewContent')
        userid = request.session.get('userid')
        print(id)
        MessageModel.objects.create(car_id=id,message=reviewContent,user_id=userid,messageDate=date.today)
        return redirect(reverse('car:buy',kwargs={'id':id}))

