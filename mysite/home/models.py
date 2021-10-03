from django.db import models

# Create your models here.


class Hobbies(models.Model):

    def __str__(self):
        myHobbies = self.hobby_name + ":&nbsp;" + self.hobby_desc + "<br><br>"
        return myHobbies

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=400)
    hobby_image = models.CharField(max_length=500, default="https://wikiclipart.com/wp-content/uploads/2018/02/Child-thinking-reflection-thinking-pencil-and-in-color-reflection-clip-art.jpg")


class Portfolios(models.Model):

    def __str__(self):
        myportfolio = self.portfolio_name + ":&nbsp;" + self.portfolio_desc + "<br><br>"
        return myportfolio

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=400)
    portfolio_image = models.CharField(max_length=500, default="https://techcrunch.com/wp-content/uploads/2015/04/codecode.jpg?w=990&crop=1")