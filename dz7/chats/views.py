from django.contrib.auth import get_user_model
from django.contrib.messages.storage.cookie import MessageSerializer
from django.shortcuts import get_object_or_404

from rest_framework import generics

from users.models import User
from .serializers import ChatSerializer, ChatListSerializer, MessageListSerializer, MessageReadStatusSerializer, \
    ChatMemberSerializer
from models import Chats


class UserChatsQuerySet:
    def get_queryset(self):
        return Chats.objects.filter(author=self.request.user)


'''For chats'''


class ChatList(UserChatsQuerySet, generics.ListAPIView):
    serializer_class = ChatListSerializer


class ChatCreate(generics.CreateAPIView):
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ChatRetrieveUpdateDestroy(
    UserChatsQuerySet, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ChatSerializer


class ChatMemberCreate(generics.CreateAPIView):
    serializer_class = ChatMemberSerializer

    def perform_create(self, serializer):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chats, pk=chat_pk)
        serializer.save(chat=chat)


class ChatMemberDestroy(generics.DestroyAPIView):
    serializer_class = ChatMemberSerializer
    lookup_field = "chat_id"
    lookup_url_kwarg = "chat_pk"

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        user = get_object_or_404(get_user_model(), pk=user_pk)
        return User.objects.filter(user=user)


'''For messages'''


class ChatMessagesQuerySet:
    def get_queryset(self):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chats, pk=chat_pk)
        return chat.chat_messages


class MessageList(ChatMessagesQuerySet, generics.ListAPIView):
    serializer_class = MessageListSerializer


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chats, pk=chat_pk)
        serializer.save(chat=chat, author=self.request.user)


class MessageRetrieveUpdateDestroy(
    ChatMessagesQuerySet, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = MessageSerializer


class MessageReadStatus(ChatMessagesQuerySet, generics.UpdateAPIView):
    serializer_class = MessageReadStatusSerializer
