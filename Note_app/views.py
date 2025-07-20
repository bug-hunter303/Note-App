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