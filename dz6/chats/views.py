from datetime import datetime
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Chats, Messages
from users.models import User


@require_GET
def chat_list(request):
    chats = Chats.objects.all().values()
    return JsonResponse({'chats': list(chats)})


@require_GET
def chat_detail(request, chat_id):
    try:
        get_chat_it = get_object_or_404(Chats, author=chat_id)
        return JsonResponse({'chat details:': list(get_chat_it)}, status=201)
    except IndexError:
        return HttpResponse(status=404)


@require_GET
def message_detail(request, mes_id):
    try:
        get_mes_it = list(Chats.objects.filter(id=mes_id).values())
        return JsonResponse({'chat details:': list(get_mes_it)}, status=201)
    except IndexError:
        return HttpResponse(status=404)


@require_POST
@csrf_exempt
def create_chat(request):
    data = request.POST
    title = data.get('title')
    new_chat = Chats(title=title)
    new_chat.save()
    return JsonResponse({'created chat:': new_chat}, status=201)


@require_POST
@csrf_exempt
def create_mes(request):
    data = request.POST
    title = data.get('title')
    new_mes = Messages(message_text=title)
    chat_id = data.get("chatId")
    sender_id = data.get("senderId")

    chat_to_find = get_object_or_404(Chats, chat=chat_id)
    author_in_chat = get_object_or_404(Chats, author=sender_id)

    if chat_to_find.users.filter(id=sender_id).exists():
        first_user = get_object_or_404(User, id=author_in_chat)
        message = Messages(chat=chat_to_find,
                           author=first_user,
                           message_text=new_mes,
                           creation_date=datetime.now())
        message.save()

        return JsonResponse({"Message created": True}, status=201)

    return JsonResponse({"created": False}, status=400)


@require_http_methods(["DELETE"])
@csrf_exempt
def delete_chat(request, chat_id):
    data = get_object_or_404(Chats, id=chat_id)
    deleting_chat_it = list(Chats.objects.filter(id=chat_id).values())
    data.delete()
    return JsonResponse({'successfully deleted this chat:': list(deleting_chat_it)}, status=201)


@require_http_methods(["DELETE"])
@csrf_exempt
def delete_mes(request, mes_id):
    data = get_object_or_404(Chats, id=mes_id)
    deleting_mes_it = list(Messages.objects.filter(id=mes_id).values())
    data.delete()
    return JsonResponse({'successfully deleted this message:': list(deleting_mes_it)}, status=201)


''' Отсюда новые'''


@require_http_methods(["PATCH"])
@csrf_exempt
def edit_chat_name(request, id_chat):
    new_name = json.loads(request.body).get("new_name")
    chat = get_object_or_404(Chats, id=id_chat)
    del_name = chat.title
    chat.title = new_name
    chat.save()
    return JsonResponse({f'chat {del_name} were renamed into {new_name}'}, status=201)


@require_http_methods(["PATCH"])
@csrf_exempt
def edit_chat_description(request, id_chat):
    new_description = json.loads(request.body).get("new_description")
    chat = get_object_or_404(Chats, id=id_chat)
    del_description = chat.description
    chat.title = new_description
    chat.save()
    return JsonResponse({f'chat description {del_description} were renamed into {new_description}'}, status=201)


@require_http_methods(["PATCH"])
@csrf_exempt
def edit_chat_mes(request, id_mes):
    new_mes = json.loads(request.body).get("new_message")
    message = get_object_or_404(Messages, id=id_mes)
    message_text = message.message
    message.message = new_mes
    message.save()
    return JsonResponse({
        "message": f"Successfully efit {message_text} to {new_mes}"
    }, status=200)


@require_http_methods(["PATCH"])
@csrf_exempt
def add_member_to_chat(request, chat_id):
    data = request.POST
    member_id = data.get("memberId")
    chat = get_object_or_404(Chats, id=chat_id)
    user = get_object_or_404(User, id=member_id)
    if not Chats.objects.filter(id=chat_id, users__in=[member_id]).exists():
        chat.users.add(user)
        chat.save()
        return JsonResponse({
            "message": f"Successfully added new member with id: {member_id}"
        }, status=200)
    else:
        return JsonResponse({
            "message": f"User with id: {member_id} is already in chat!"
        }, status=400)


@require_http_methods(["PATCH"])
@csrf_exempt
def kick_member_from_chat(request, chat_id):
    user_id_to_kick = json.loads(request.body).get("id")
    chat = get_object_or_404(Chats, id=chat_id)
    user = get_object_or_404(User, id=user_id_to_kick)
    if Chats.objects.filter(id=chat_id, users__in=[user_id_to_kick]).exists():
        chat.users.remove(user)
        chat.save()
        return JsonResponse({
            "message": f"Successfully deleted member! id: {user_id_to_kick}"
        }, status=200)
    else:
        return JsonResponse({
            "message": f"User with this id: {user_id_to_kick} is not in the current chat!"
        }, status=400)


@require_GET
def chat_messages(request, chat_id):
    messages = get_object_or_404(Messages.objects.filter(chat=chat_id))
    if messages:
        return JsonResponse({
            "messages": [
                {
                    "chat": message.chat,
                    "message_text": message.message_text,
                    "author": message.author.username,
                    "is_read": message.is_read,
                    "creation_date": message.creation_date
                }
                for message in messages
            ]
        }, status=200)
    else:
        return JsonResponse({
            "message": f"Messages weren't found. Try to check your chat id: {chat_id}"
        }, status=400)


@require_http_methods(["PATCH"])
@csrf_exempt
def make_read(request, chat_id):
    mes_id = json.loads(request.body).get("mesId")
    message = get_object_or_404(Messages.objects.filter(chat=chat_id, id=mes_id))
    message.is_read = True
    message.save()
    return JsonResponse({f'done'}, status=201)
