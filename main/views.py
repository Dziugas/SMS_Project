from django.shortcuts import render, get_object_or_404
from .models import Notes


def index(request):
    all_notes = Notes.objects.all()
    return render(request, 'main/index.html', {'all_notes' : all_notes})


def detail(request, note_id):
    note = Notes.objects.get(pk=note_id)
    return render(request, 'main/detail.html', {'note' : note})