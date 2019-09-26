from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def who(request):
    return render(request, 'who.html')

def contact(request):
    return render(request, 'contact.html')

def codeofconduct(request):
    return render(request, 'codeofconduct.html')
