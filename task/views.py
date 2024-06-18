from django.shortcuts import render,redirect
from . import forms
from . import models


# Create your views here.
def create_task(request):
    if request.method == "POST":
        task = forms.task_form(request.POST)
        if task.is_valid():
            task.save()
            return redirect('index')
            

    else:
        task  = forms.task_form()

    return render(request,'task.html',{'form': task })

def Edit_text(request,id):    
    task = models.task.objects.get(pk=id) 
    edit_form = forms.task_form(instance=task)
    if request.method == "POST":

        edit_form = forms.task_form(request.POST,instance=task)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('index')
    else:
        task  = forms.task_form()

    return render(request,'task.html',{'form': edit_form })   

def delete(request, id):
    post = models.task.objects.get(pk=id) 
    post.delete()
    return redirect('index')