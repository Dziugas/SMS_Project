from django.shortcuts import render, get_object_or_404
from .models import SmsContent


def index(request):
    all_sms = SmsContent.objects.all()
    return render(request, 'main/index.html', {'all_sms' : all_sms})


def detail(request, sms_id):
    sms = get_object_or_404(SmsContent, pk='sms_id')
    return render(request, 'main/detail.html', {'sms' : sms})