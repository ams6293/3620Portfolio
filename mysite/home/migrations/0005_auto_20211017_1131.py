# Generated by Django 2.2 on 2021-10-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211002_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbies',
            name='hobby_image',
            field=models.CharField(default='https://cdn.onlinewebfonts.com/svg/img_98811.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='portfolios',
            name='portfolio_image',
            field=models.CharField(default='https://tse2.mm.bing.net/th?id=OIP.nJsz6Wn-DX7zM9dW5hDzBwAAAA&pid=Api&P=0&w=229&h=167', max_length=500),
        ),
    ]