from django import forms
from .models import Hobbies
from .models import Portfolios


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields = ['hobby_name', 'hobby_desc', 'hobby_image']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolios
        fields = ['portfolio_name', 'portfolio_desc', 'portfolio_image']