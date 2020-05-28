from django.shortcuts import render
from .models import Details
# Create your views here.


def index(request):
    data=Details.objects.all()
    for vdo in data:
        list=vdo.Youtube_link.split('/')
        vdo.video_id=list[len(list)-1]


    return render(request,'index.html',{'data':data})

def go(request):
    name=request.GET['name']
    lastname=request.GET['lastname']
    password=request.GET['password']
    return render(request,'go.html',{'firstname':name,'lastname':lastname})
