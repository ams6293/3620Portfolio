
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="portfolio"),
    path('contact/', views.contact, name="contact")
]