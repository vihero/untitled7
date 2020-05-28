from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method=="POST":
        print('hieee')
        usern=request.POST['username']
        passw=request.POST['password']
        print(usern,passw)
        user=auth.authenticate(username=usern,password=passw)
        print(user)
        if user is not None:
            auth.login(request,user)
            print('valid user')
            return render(request, 'index.html')
        else:
            print('invalid user')
            return redirect('/')
    else:
        print('hello')
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first=request.POST['first']
        last = request.POST['last']
        user = request.POST['user']
        passw = request.POST['pass']
        cpass = request.POST['cpass']
        email = request.POST['email']
        print('hiee')

        user=User.objects.create_user(first_name=first,last_name=last,username=user,email=email)
        user.save();
        print('user Created')
        return render(request,'login.html')
    else:
        return render(request,'register.html')