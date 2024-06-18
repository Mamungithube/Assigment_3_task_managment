from django import forms
from .models import Category

class categiory_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'