from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['psw']
        cpassword = request.POST['psw-repeat']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user Name already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "user mail already exist")
                return redirect('register')
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                        password=password)
            user.save();
            return redirect('login')
        else:
            messages.info(request,"password not mathing")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

