from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.create_catagory,name='create_catagory'),
]
