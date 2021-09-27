from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Have a welcome message, general summary about yourself')

def contact(request):
    return HttpResponse('<b>Amber Spatig:</b> amberspatig@mail.weber.edu')