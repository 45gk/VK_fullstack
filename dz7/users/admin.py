from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "birthday", "status", "hobbies", "phone_num",
                    "home_city")
    ordering = ["id"]
# Register your models here.
