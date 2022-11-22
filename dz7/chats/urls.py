from django.urls import path

from chats.views import ChatMemberCreate, ChatCreate, ChatList, ChatRetrieveUpdateDestroy, ChatMemberDestroy, \
    MessageList, MessageCreate, MessageRetrieveUpdateDestroy, MessageReadStatus

urlpatterns = [
    path("", ChatList.as_view(), name="chat_list"),
    path("new/", ChatCreate.as_view(), name="chat_create"),
    path("<int:pk>/", ChatRetrieveUpdateDestroy.as_view(), name="chat_detail"),
    path("<int:chat_pk>/members/new/", ChatMemberCreate.as_view(), name="chat_member_create"),
    path("<int:chat_pk>/members/<int:id_pk>/", ChatMemberDestroy.as_view(), name="chat_member_delete"),
    path("<int:chat_pk>/messages/", MessageList.as_view(), name="message_list"),
    path("<int:chat_pk>/messages/new/", MessageCreate.as_view(), name="message_create"),
    path("<int:chat_pk>/messages/<int:pk>/", MessageRetrieveUpdateDestroy.as_view(), name="message_detail"),
    path("<int:chat_pk>/messages/<int:pk>/mark_read/", MessageReadStatus.as_view(), name="message_read"),
]