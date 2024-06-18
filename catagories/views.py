from django.shortcuts import render,redirect
from . import forms


# Create your views here.
def create_catagory(request):
    if request.method == "POST":
        category = forms.categiory_form(request.POST)
        if category.is_valid():
            category.save()
            return redirect('index')
            

    else:
        category  = forms.categiory_form()

    return render(request,'category.html',{'form': category })