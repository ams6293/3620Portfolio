from django.db import models

# Create your models here.


class Hobbies(models.Model):

    def __str__(self):
        myHobbies = self.hobby_name + ":&nbsp;" + self.hobby_desc + "<br><br>"
        return myHobbies

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=400)
    hobby_image = models.CharField(max_length=500, default="https://cdn.onlinewebfonts.com/svg/img_98811.png")


class Portfolios(models.Model):

    def __str__(self):
        myportfolio = self.portfolio_name + ":&nbsp;" + self.portfolio_desc + "<br><br>"
        return myportfolio

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=400)
    portfolio_image = models.CharField(max_length=500, default="https://tse2.mm.bing.net/th?id=OIP.nJsz6Wn-DX7zM9dW5hDzBwAAAA&pid=Api&P=0&w=229&h=167")