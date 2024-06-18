from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.create_task,name='create_task'),
    path('edit/<int:id>', views.Edit_text, name='Edit_text'),
    path('delete/<int:id>', views.delete, name='delete'),
]
