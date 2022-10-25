from django.urls import path
from chats.views import chat_list, chat_detail, create_chat

urlpatterns = [
    path('', chat_list, name='chat_list'),
    #path('category/<int:pk>/', chat_category, name='chat_category'),
    path('chat_detail/<int:chat_id>/', chat_detail, name='chat_detail'),
    path('create_chat/', create_chat, name='create_chat'),

]