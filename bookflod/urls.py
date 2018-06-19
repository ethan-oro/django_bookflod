from django.contrib import admin
from django.urls import path
from bookflod.views import home

urlpatterns = [
    path('', home),
]
