from django.shortcuts import render, redirect
from .models import Notes
from .forms import NoteForm


def index(request):
    all_notes = Notes.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
    else:
        form = NoteForm()
    return render(request, 'main/index.html', {'all_notes' : all_notes, 'form' : form})


def detail(request, note_id):
    note = Notes.objects.get(pk=note_id)
    return render(request, 'main/detail.html', {'note' : note})