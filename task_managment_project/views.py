from django.shortcuts import render
from task.models import task

def home(request):
    data = task.objects.all()
    return render(request, 'index.html', {'data' : data})