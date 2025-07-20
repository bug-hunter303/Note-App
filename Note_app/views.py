from django.shortcuts import render
from Note_app.models import Notes
from django.http import HttpResponseRedirect

# Create your views here.


def display_note(request):
    notes = Notes.objects.all()
    return render(
        request,
        "display_note.html",
        {"notes": notes},
    )
    
def edit_note(request,id):
    note = Notes.objects.get(id = id)
    return render(
        request,
        "edit_note.html",
        {"note": note},
    )
    