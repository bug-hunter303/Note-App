from django.shortcuts import render
from Note_app.models import Notes
from django.http import HttpResponseRedirect

# Create your views here.


def display_note(request):
    note = Notes.objects.all()
    return render(
        request,
        "display_note.html",
        {"note": note},
    )