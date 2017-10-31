from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    twiml = '<Response><Message>responsas</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')