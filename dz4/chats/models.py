from django.db import models




class Chats(models.Model):
    users = models.ManyToManyField('Users')


class Users(models.Model):
    name = models.CharField(max_length=30)


class Messages(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    chat = models.ForeignKey('Chats', on_delete=models.CASCADE)
    creation_time = models.TimeField()
    content = models.CharField(max_length=255)
