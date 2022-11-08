from datetime import datetime


from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .models import Chats, Messages
from users.models import User


def chat_list(request):
    # render()
    if request.method == "GET":
        chats = Chats.objects.all().values()
        return JsonResponse({'chats': list(chats)})
    else:
        return HttpResponse(status=405)


def chat_detail(request, chat_id):
    if request.method == "GET":
        try:
            get_chat_it = list(Chats.objects.filter(id=chat_id).values())
            return JsonResponse({'chat details:': list(get_chat_it)}, status=201)
        except IndexError:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


def message_detail(request, mes_id):
    if request.method == "GET":
        try:
            get_mes_it = list(Chats.objects.filter(id=mes_id).values())
            return JsonResponse({'chat details:': list(get_mes_it)}, status=201)
        except IndexError:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        new_chat = Chats(title=title)
        new_chat.save()
        new_chat_id = new_chat.id
        new_chat_iterable = Chats.objects.filter(id=new_chat_id).values()
        return JsonResponse({'chats': list(new_chat_iterable)}, status=201)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def create_mes(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        new_mes = Messages(message_text=title)
        chat_id = data.get("chatId")
        sender_id = data.get("senderId")

        chat = get_object_or_404(Chats, chat=chat_id)
        author = get_object_or_404(Chats, author=sender_id)

        if new_mes and sender_id in (chat.first_user.id, chat.second_user.id):
            first_user = get_object_or_404(User, id=author)
            message = Messages(chat=chat,
                               author=first_user,
                               message_text=new_mes,
                               creation_date=datetime.now())
            message.save()

            return JsonResponse({"Message created": True}, status=201)

        return JsonResponse({"created": False}, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def delete_chat(request, chat_id):
    if request.method == "DELETE":
        data = get_object_or_404(Chats, id=chat_id)
        deleting_chat_it = list(Chats.objects.filter(id=chat_id).values())
        data.delete()
        return JsonResponse({'successfully deleted this chat:': list(deleting_chat_it)}, status=201)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def delete_mes(request, mes_id):
    if request.method == "DELETE":
        data = get_object_or_404(Chats, id=mes_id)
        deleting_mes_it = list(Messages.objects.filter(id=mes_id).values())
        data.delete()
        return JsonResponse({'successfully deleted this message:': list(deleting_mes_it)}, status=201)
    else:
        return HttpResponse(status=405)

