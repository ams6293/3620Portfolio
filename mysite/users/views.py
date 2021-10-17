from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == 'post':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account is created.')
            return redirect('home:portfolio')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})
