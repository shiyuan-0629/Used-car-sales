from django.shortcuts import render
from notice.models import *
# Create your views here.
def notice(request):
    return render(request,"notice.html",{"notice":NoticeModel.objects.all().order_by('-date')})