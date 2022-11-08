from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from users.views_utils import serialize_response_data

from users.models import User


@require_http_methods(['GET'])
def user_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    json_response = serialize_response_data(user,
                                            fields=['username',
                                                    'first_name',
                                                    'last_name',
                                                    'birthday',
                                                    'status',
                                                    'hobbies',
                                                    'phone_num',
                                                    'home_city',
                                                    'chats'])
    return JsonResponse({'user': json_response})


@require_http_methods(['GET'])
def chats_list(request, user_id):
    chats = get_object_or_404(User, id=user_id).chats.all()
    json_response = serialize_response_data(chats)
    return JsonResponse({'chats': json_response})


@require_http_methods(['GET'])
def messages_list(request, user_id):
    chats = get_object_or_404(User, id=user_id).messages.all()
    json_response = serialize_response_data(chats)
    return JsonResponse({'chats': json_response})