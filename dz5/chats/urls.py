from django.urls import path
from chats.views import chat_list, chat_detail, create_chat, create_mes, delete_mes, delete_chat

urlpatterns = [
    path('', chat_list, name='chat_list'),

    path('chat_detail/<int:chat_id>/', chat_detail, name='chat_detail'),
    path('create_chat/', create_chat, name='create_chat'),
    path('create_message/', create_mes, name='create_message'),
    path('delete_chat/<int:chat_id>/', delete_chat, name='delete_chat'),
    path('delete_message/<int:mes_id>/', delete_mes, name='delete_message'),
]