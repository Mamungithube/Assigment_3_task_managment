from django.shortcuts import render,redirect
from . import forms


# Create your views here.
def create_task(request):
    if request.method == "POST":
        task = forms.task_form(request.POST)
        if task.is_valid():
            task.save()
            return redirect('create_task')
            

    else:
        task  = forms.task_form()

    return render(request,'task.html',{'form': task })