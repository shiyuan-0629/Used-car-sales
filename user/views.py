from django.shortcuts import render, redirect
from django.urls import reverse

from user.models import UserModel


def info(request):
    return render(request,'info.html',{"default":"user:accountInfo"})

def accountInfo(request):
    userid = request.session.get('userid')
    user = UserModel.objects.get(id=userid)
    return render(request,'account_info.html',{'user':user})

def favoriteInfo(request):
    return redirect(reverse("favorites:favorites"))

def orderInfo(request):
    return redirect(reverse("order:order"))

def loginInfo(request):
    return redirect(reverse("system:loginlist"))
