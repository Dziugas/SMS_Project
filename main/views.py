from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NoteForm, DeleteNote


def index(request):
    all_notes = Notes.objects.all().order_by('-date')
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('main:detail', note.id)
    else:
        form = NoteForm()
    return render(request, 'main/index.html', {'all_notes' : all_notes, 'form' : form})


def detail(request, note_id):
    note = Notes.objects.get(pk=note_id)
    form = DeleteNote()
    return render(request, 'main/detail.html', {'note' : note, 'form' : form})


def delete_note(request, note_id):
    note_to_delete = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = DeleteNote(request.POST, instance=note_to_delete)
        if form.is_valid():
            note_to_delete.delete()
            return redirect('main:index')
    else:
        form = DeleteNote(instance=note_to_delete)
    return render(request, 'main/index.html', {'form' : form})

def note_edit(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('main:detail', note_id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'main/index.html', {'form':form})

