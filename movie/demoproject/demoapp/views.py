from django.http import HttpResponse
from django.shortcuts import render
from .models import destinations, members


# Create your views here.
def demo(request):
    obj=destinations.objects.all()
    obj1=members.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

#def about(request):
    #return render(request,"about.html")

#def gallery(request):
    #return render(request,"gallery.html")

#def login(request):
    #return render(request,"login.html")
#def contact(request):
    #return render(request,"contact.html")
