from django.db import models

# Create your models here.


class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=400)

