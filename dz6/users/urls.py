from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('info/<int:user_id>/', views.user_info, name='user_info'),
    path('chats/<int:user_id>/', views.chats_list, name='chats_list'),
    path('messages/<int:user_id>/', views.messages_list, name='messages_list')

]