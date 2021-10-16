
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/<int:hobby_id>', views.hobbyDetail, name="hobbyDetail"),
    path('contact/', views.contact, name="contact"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:portfolio_id>', views.portfolioDetail, name="portfolioDetail"),
    path('hobbies/add', views.create_hobby, name="create_hobby"),
    path('portfolio/add', views.create_portfolio, name="create_portfolio"),
    path('portfolio/update/<int:id>', views.update_portfolio, name="update_portfolio"),
    path('hobbies/update/<int:id>', views.update_hobby, name="update_hobby"),
    path('hobbies/delete/<int:id>', views.delete_hobby, name="delete_hobby"),
    path('portfolio/delete/<int:id>', views.delete_portfolio, name="delete_portfolio")
]