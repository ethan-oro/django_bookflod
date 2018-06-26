from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView
from bookflod.models import UserProfile, Book
#series of funciton / classea that take data and display them on the page

class HomeView(ListView) :
    model = UserProfile
    template_name ='home.html'

class UserView(View) :
    model = UserProfile

class UserList(UserView, ListView) :
    template_name='userprofiles.html'

class UserDetail(UserView, DetailView) :
    pass

class UserCreate(UserView, CreateView) :
    fields = ['user', 'dob', 'country', 'books_read', 'books_wanted', 'genre', 'languages']

class BookView(UserView, View) :
    model = Book

class BookList(BookView, ListView) :
    template_name='books.html'

class BookDetail(BookView, DetailView) :
    pass

class BookCreate(BookView, CreateView) :
    fields = ['title', 'author', 'genre', 'isbn', 'language']
