from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello World!!!")

def Login(request):
    return render(request, 'Paginas/Login.html')