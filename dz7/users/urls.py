from django.urls import path

from users.views import UserInfo

urlpatterns = [
    path("user/<int:pk>", UserInfo.as_view()),
]