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
