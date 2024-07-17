from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    return render(request, 'home.html')
 
def register(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def forgot(request):
    return render(request, 'forgot.html')

def pwdupdate(request):
    return render(request, 'pwdupdate.html')

def save_for(request):
    return render(request, 'save_for.html')

def help(request):
    return render(request, 'help.html')

def certificate(request):
    return render(request, 'certificate.html')