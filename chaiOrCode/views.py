from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render (request,'index.html')

def about(request):
    return HttpResponse("Saqib About")

def contact(request):
    return HttpResponse("Saqib contact")

