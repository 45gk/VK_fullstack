import datetime

from django.conf import settings
from django.db import models
from users.models import User


class Chats(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название чата', default="Default title")
    description = models.TextField(blank=True, verbose_name='Описание чата')
    members = models.ManyToManyField(User, related_name='chat_user', verbose_name="Участники")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания чата')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.title


class Messages(models.Model):
    chat = models.ForeignKey(
        Chats,
        on_delete=models.CASCADE,
        default=None,
        verbose_name='Чат, в котором находится сообщение')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Отправитель сообщения')
    message_text = models.TextField(verbose_name='Текст сообщения', default="Default mes")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания сообщения')
    is_read = models.BooleanField(default=False,
                                  null=False,
                                  verbose_name="Прочитано")


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
