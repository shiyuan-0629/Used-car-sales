from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse


from Utils.password import *
from system.models import SystemModel
from user.models import UserModel


# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel.objects.filter(name=name)
        if user.exists():
            user = user.first()
            if verify_md5(password, user.password):
                request.session['userid'] = user.id
                SystemModel.objects.create(state="success",user_id=user.id,type="login",lastDate=date.today())
                return redirect(reverse("car:cars"))
            else:
                SystemModel.objects.create(state="fail", user_id=user.id, type="login", lastDate=date.today())
                return render(request, 'login.html', {"message": "密码错误"})
        else:
            SystemModel.objects.create(state="fail", user_id=user.id, type="login", lastDate=date.today())
            return render(request, 'login.html',{"message":"用户不存在"})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            user = UserModel.objects.filter(name=name, password=password)
            if user.exists():
                return render(request, 'register.html', {"message": "账号已存在"})
            else:
                password = generate_md5(password)
                UserModel.objects.create(name=name, password=password,balance=0)
                return redirect(reverse("system:login"))
        else:
            return render(request, 'register.html', {"message": "两次密码不一致"})
    else:
        return render(request, 'register.html')

def loginlist(request):
    userid = request.session.get('userid')
    loginList = SystemModel.objects.filter(user_id=userid,type='login').order_by("-lastDate")
    return render(request,"login_info.html",{"loginList":loginList})

def logout(request):
    userid = request.session.get('userid')
    SystemModel.objects.create(state="success", user_id=userid, type="logout", lastDate=date.today())
    request.session.flush()
    return redirect(reverse("system:login"))

def updatepwd(request):
    userid = request.session.get('userid')
    password = request.POST.get('newPassword')
    password = generate_md5(password)
    UserModel.objects.update(password=password)
    SystemModel.objects.create(state="success", user_id=userid, type="logout", lastDate=date.today())
    request.session.flush()
    return redirect(reverse("system:login"))
