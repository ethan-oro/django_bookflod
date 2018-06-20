from django.contrib import admin
from django.urls import path
from bookflod.views import home, books, user_profiles

urlpatterns = [
    path('', home),
    path('books', books),
    path('userprofiles', user_profiles),
]
