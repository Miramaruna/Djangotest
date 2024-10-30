from django.db import models

# Create your models here.

class Main(models.Model):
    Name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    Text = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )