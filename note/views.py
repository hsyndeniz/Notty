from django.shortcuts import render, HttpResponse
from .models import Note

# Create your views here.
def note(request):
    notes = Note.objects.all()
    return render(request, "examples/dashboard.html", {'notes': notes})

def profile(request):
    return render(request, "examples/user.html")