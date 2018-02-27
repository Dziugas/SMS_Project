from django.shortcuts import render, get_object_or_404
from .models import Notes
from .forms import NoteForm


def index(request):
    all_notes = Notes.objects.all()
    form = NoteForm
    return render(request, 'main/index.html', {'all_notes' : all_notes, 'form' : form})


def detail(request, note_id):
    note = Notes.objects.get(pk=note_id)
    return render(request, 'main/detail.html', {'note' : note})