from django.http import Http404

from rest_framework import serializers

from .models import Chats, Messages
from users.models import User

ALL_CHAT_FIELDS = ["id", "title", "description", "members", "creation_date"]
ALL_MES_FIELDS = ["id", "author", "chat", "message_text", "creation_date", "is_read"]


'''For chats'''


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    def create(self, validated_data):
        chat = Chats.objects.create(**validated_data)

        user = validated_data.get("author")
        User.objects.create(chat=chat, user=user)

        return chat

    class Meta:
        model = Chats
        fields = ["id", "title", "description", "members", "creation_date"]


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ["id", "title", "description", "members"]


class ChatMemberSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.get("user")
        chat = validated_data.get("chat")

        chat_member = User.objects.filter(chat=chat, user=user).first()
        if chat_member:
            raise Http404(f"This user: {user} is already in the chat {chat}!")

        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ["chat", "user"]


'''For messages'''


class MessageListSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Messages
        fields = ["id", "author", "chat", "message_text", "creation_date "]


class MessageReadStatusSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    def update(self, instance, validated_data):
        instance.is_read = True
        instance.save()
        return instance

    class Meta:
        model = Messages
        fields = ALL_MES_FIELDS


class MessageListSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Messages
        fields = ["id", "author", "chat", "message_text"]
