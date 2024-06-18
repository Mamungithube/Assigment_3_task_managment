from django import forms
from .models import task

class task_form(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
        widgets={
            'Task_Assign_Date': forms.NumberInput(attrs={'type':'date'}),

        }