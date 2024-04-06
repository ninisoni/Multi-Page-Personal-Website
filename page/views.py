from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'page/home.html')

def about(request):
    return render(request, 'page/about.html') 

def contact(request):
    if request.method == 'POST':
        return redirect('welcome')
    return render(request, 'page/contact.html')

def welcome(request):
    return HttpResponse("Welcome! Your message has been received.")


