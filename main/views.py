from django.shortcuts import render, get_object_or_404
from .models import Notes


def index(request):
    all_sms = Notes.objects.all()
    return render(request, 'main/index.html', {'all_notes' : all_notes})


def detail(request, note_id):
    notes = get_object_or_404(Notes, pk='note_id')
    return render(request, 'main/detail.html', {'notes' : notes})