from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolios
from .forms import HobbyForm
from .forms import PortfolioForm
from django.template import loader


# Create your views here.


def home(request):
    context = {}
    return render(request, 'home/index.html', context)


def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)


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


def create_hobby(request):
    form = HobbyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('hobbies')

    return render(request, 'home/hobbies/hobby-form.html', {'form': form})


def update_hobby(request, id):
    hobbyitem = Hobbies.objects.get(id=id)
    form = HobbyForm(request.POST or None, instance=hobbyitem)

    if form.is_valid():
        form.save()
        return redirect('hobbies')

    return render(request, 'home/hobbies/hobby-form.html', {'form': form, 'hobby': hobbyitem})


def delete_hobby(request, id):
    hobby = Hobbies.objects.get(id=id)

    if request.method == 'POST':
        hobby.delete()
        return redirect('hobbies')

    return render(request, 'home/hobbies/hobby-delete.html', {'hobby': hobby})


def create_portfolio(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolio')

    return render(request, 'home/portfolio/portfolio-form.html', {'form': form})


def update_portfolio(request, id):
    portfolioitem = Portfolios.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=portfolioitem)

    if form.is_valid():
        form.save()
        return redirect('portfolio')

    return render(request, 'home/portfolio/portfolio-form.html', {'form': form, 'portfolio': portfolioitem})


def delete_portfolio(request, id):
    portfolio = Portfolios.objects.get(id=id)

    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio')

    return render(request, 'home/portfolio/portfolio-delete.html', {'portfolio': portfolio})