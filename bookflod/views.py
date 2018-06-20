from django.shortcuts import render
from bookflod.models import UserProfile, Book
#series of funciton / classea that take data and display them on the page


def books(request) :
    all_books = Book.objects.all()
    data = { 'books' : all_books }
    return render(request, 'books.html', data)

def home(request) :
    return render(request, 'home.html')

def user_profiles(request) :
    user_profiles = UserProfile.objects.all()
    data = { 'profiles' : user_profiles }
    return render(request, 'userprofiles.html', data)
