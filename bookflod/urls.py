from django.contrib import admin
from django.urls import path
from bookflod.views import home, books, user_profiles

app_name = "bookflod"

urlpatterns = [
    path('', home),
    path('books', books, name = 'books'),
    path('userprofiles', user_profiles),
]
