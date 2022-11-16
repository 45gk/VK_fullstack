from django.contrib import admin
from chats.models import Messages, Chats
from users.models import User

admin.site.register(Messages)
admin.site.register(Chats)
admin.site.register(User)
# Register your models here.
