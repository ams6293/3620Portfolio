from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolios

# Create your views here.


def home(request):
    return HttpResponse('My name is Amber Spatig. I\'m a senior here at WSU and my major is computer science. I want to'
                        'be a front end web developer one day. ')


def contact(request):
    return HttpResponse('<b>Amber Spatig:</b> amberspatig@mail.weber.edu')


def hobbies(request):

    
    hobby_list = Hobbies.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):

    portfolio_list = Portfolios.objects.all()
    return HttpResponse(portfolio_list)
