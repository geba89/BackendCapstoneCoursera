from django.contrib import admin
from django.urls import path
from .views import say_hello, index

urlpatterns = [
    path('hello', say_hello, name='say_hello'),
    path('', index, name="index")
]