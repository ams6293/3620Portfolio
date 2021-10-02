
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/<int:hobby_id>', views.hobbyDetail, name="hobbyDetail"),
    path('contact/', views.contact, name="contact"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:portfolio_id>', views.portfolioDetail, name="portfolioDetail")
]