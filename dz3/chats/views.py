from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

chat_list1 = [
    {
        "chat_id": 1,
        "title": "sda"
    }
]


# Create your views here.
def chat_list(request):
    # render()
    if request.method == "GET":

        return JsonResponse({'chats': chat_list1})
    else:
        return HttpResponse(status=405)





def chat_detail(request, chat_id):
    if request.method == "GET":
        try:
            return JsonResponse({'chat_detail': chat_list1[int(chat_id)-1]})
        except IndexError:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        chat_list1.append({"chat_id": len(chat_list1), "title": request.POST.get('title')})

        return JsonResponse({'chats': chat_list1}, status=201)
    else:
        return HttpResponse(status=405)



