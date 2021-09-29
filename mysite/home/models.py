from django.db import models

# Create your models here.


class Hobbies(models.Model):

    def __str__(self):
        myHobbies = self.hobby_name + ":&nbsp;" + self.hobby_desc + "<br><br>"
        return myHobbies

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=400)


class Portfolios(models.Model):

    def __str__(self):
        myportfolio = self.portfolio_name + ":&nbsp;" + self.portfolio_desc + "<br><br>"
        return myportfolio

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=400)