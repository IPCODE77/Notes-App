from django.shortcuts import render,redirect
from django.http import HttpResponse  
from user.models import *

# Create your views here.


def take_notes(request):
    if request.method == 'POST':
        data = request.POST
        notetittles = data.get('notetittle')
        notesdescc = data.get('notedesc')
        if len(notetittles)>=1 and len(notesdescc)>=1:
            notepad.objects.create(
                note_tittle = notetittles,
                note_desc = notesdescc
            )
        return redirect('/home')
    # querset = notepad.objects.all()
    allnote = notepad.objects.all()
    if request.GET.get('search'):
        allnote = allnote.filter(note_tittle__icontains = request.GET.get('search'))
    context = {'allnote':allnote}
    return render(request,'html/notes.html',context) 


def cancel_item(request , id):
    queryselete = notepad.objects.get(id=id)
    queryselete.delete()
    return redirect('/home')


def edit_item(request , id):
    queryset = notepad.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        notetittle = data.get('notetittle')
        notedesc = data.get('notedesc')
        queryset.note_tittle = notetittle
        queryset.note_desc = notedesc

        queryset.save()
        return redirect('/home')
    context = {'note':queryset}
    return render(request , 'html/edit.html',context)