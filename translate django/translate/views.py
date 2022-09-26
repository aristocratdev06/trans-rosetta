from django.shortcuts import render, get_object_or_404
from .models import TranslatePage


def home(request):
    
    return render(request, "home.html")

def translate(request):
    malumot = TranslatePage.objects.all()
    return render(request, "translate.html", {"malumot":malumot})