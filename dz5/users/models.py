from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthday = models.DateField(
        null=True, blank=True,
        verbose_name='Дата рождения'
    )
    status = models.TextField(
        max_length=500, null=True,
        blank=True, verbose_name='Статус'
    )
    hobbies = models.TextField(
        max_length=500, null=True,
        blank=True, verbose_name='Хобби'
    )
    phone_num = models.CharField(
        max_length=16, blank=True,
        verbose_name='Номер телефона'
    )
    home_city = models.CharField(
        max_length=150, blank=True,
        verbose_name='Город'
    )
    chats = models.ManyToManyField('chats.Chats', verbose_name='Чаты пользователя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
# Create your models here.
