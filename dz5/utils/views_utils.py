import json

from django.core.serializers import serialize


def load_request_data(request):
    data_encode = request.body.decode('utf-8')
    return json.loads(data_encode)


def serialize_response_data(data, fields=None, format='json'):
    if not hasattr(data, '__iter__'):
        data = [data]
    data_serialize = serialize(format, data, fields=fields)
    return json.loads(data_serialize)