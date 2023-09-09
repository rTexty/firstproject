from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reversed(request):
    db = request.GET['text']
    reversed_text = db[::-1]
    return render(request, 'reversed.html', {'text':db, 'reversedtext': reversed_text})