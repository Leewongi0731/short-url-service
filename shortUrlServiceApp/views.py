import json
import uuid
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ShortUrl


# Create your views here.
def default(request):
    return HttpResponse("Heelloooww. This is a short url service app!")


def get_original_url(request, short_url):
    if request.method == "GET":
        short_url_obj = ShortUrl.objects.filter(short_url=short_url).first()
        if short_url_obj is not None:
            return HttpResponseRedirect(short_url_obj.original_url)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=404)


def save_original_url_and_get_short_url(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        original_url = body_data.get('original_url')

        newId = generate_new_id()
        short_url = encode_base62(newId)
        short_url_obj = ShortUrl(
            id=newId,
            short_url=short_url,
            original_url=original_url,
        )
        short_url_obj.save()
        return JsonResponse({'short_url': short_url, 'original_url': original_url})
    else:
        return HttpResponse(status=404)


def generate_new_id():
    return uuid.uuid4().int


# base 62 encoding
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode_base62(num):
    if num == 0:
        return BASE62[0]

    encoded = []
    while num > 0:
        num, remainder = divmod(num, 62)
        encoded.insert(0, BASE62[remainder])

    return ''.join(encoded)
