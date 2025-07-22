from django.shortcuts import render,redirect
from Note_app.models import Notes
from django.http import HttpResponseRedirect
from Note_app.forms import NotesForm

# Create your views here.


def display_note(request):
    notes = Notes.objects.all()
    return render(
        request,
        "display_note.html",
        {"notes": notes},
    )

def add_note(request):
    if request.method == "GET":
        form = NotesForm()
        return render(
            request,
            "add_note.html",
            {"form": form},
        )
    else:
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes-display")  # goes to your main notes page
        return render(
            request, 
            "add_note.html", 
            {"form": form}
        )
    
def delete_note(request,pk):
    note = Notes.objects.get(pk = pk)
    note.delete()
    return HttpResponseRedirect('/')

def edit_note(request , pk):
    note = Notes.objects.get(pk = pk)
    
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return HttpResponseRedirect('/')    
    else:
        return render(
            request,
            'edit_note.html',
            {'note': note}
        )