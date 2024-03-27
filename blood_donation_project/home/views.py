from django.shortcuts import render, HttpResponse
from home.models import contact as u
from datetime import datetime
from home.models import Donateblood, requestBlood
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.


def index(request):
    return render(request, "index.html")
    #return HttpResponse("'Hello'")

def about(request):
    return render(request, "about.html")    
    #return HttpResponse("'Hello'")

def register(request):
    if request.method=="POST":
        fname= request.POST.get('fullName')
        email= request.POST.get('email')
        bloodGroup= request.POST.get('bloodGroup')
        contact= request.POST.get('contactNumber')
        password= request.POST.get('password')
        re_password= request.POST.get('re_password')
        register.password=  make_password(password)
        register.re_password= make_password(re_password)
        registerCustomer= re(fname='fname', email= 'email', bloodGroup= 'bloodGroup', password= 'password', re_password= 're_password',  contactNumber= 'contacts')
        registerCustomer.save()
    return render(request, "registre.html")
    #return HttpResponse("'Hello'")

def donate(request):
    return render(request, "donate.html")
    #return HttpResponse("'Hello'")

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('fullName')
        email= request.POST.get('email')
        message= request.POST.get('message')
        conta= u(name=name, email=email, msg=message)
        conta.save()
    return render(request, "contact.html")
    #return HttpResponse("'Hello'")

def request(request):
    if request.method=="POST":
        fullname= request.POST.get("fullname")
        email= request.POST.get("email")
        bloodGroup= request.POST.get('bloodGroup')
        quantity= request.POST.get("quantity")
        urgency= request.POST.get("urgency")
        desc= request.POST.get("additionalInfo")
        contactNumber= request.POST.get("contactNumber")
        RequestBlood= requestBlood(fullname= fullname, email= email, bloodGroup= bloodGroup, quantity= quantity, urgency= urgency, desc= desc, contactNumber=contactNumber)
        RequestBlood.save()
    return render(request, "request.html")
    #return HttpResponse("'Hello'")

def donateblood(request):
    if request.method == 'POST':
        fname= request.POST.get('fullName')
        email= request.POST.get('email')
        date= request.POST.get('date')
        group= request.POST.get('bloodGroup')
        Contact= request.POST.get('contactNumber')
        donateBld= Donateblood(fname=fname, email= email, date=date, bloodGroup= group, contactNumber= Contact)
        donateBld.save()

    return render(request, "donateblood.html")