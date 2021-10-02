from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolios
from django.template import loader


# Create your views here.


def home(request):

    return HttpResponse('About Me')

def contact(request):
    return HttpResponse('<b>Amber Spatig:</b> amberspatig@mail.weber.edu')


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request,  'home/hobbies/hobbyIndex.html', context)


def hobbyDetail(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'home/hobbies/hobbyDetail.html', context)


def portfolio(request):
    portfolio_list = Portfolios.objects.all()

    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'home/portfolio/portfolioIndex.html', context)


def portfolioDetail(request, portfolio_id):
    portfolio = Portfolios.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'home/portfolio/portfolioDetail.html', context)
