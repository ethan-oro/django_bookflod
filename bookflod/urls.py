from django.contrib import admin
from django.urls import path
from bookflod import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('books', views.BookList.as_view(), name='books'),
    path('books/add', views.BookCreate.as_view(), name='addbook'),
    path('books/<pk>', views.BookDetail.as_view(), name='bookdetail'),
    path('userprofiles', views.UserList.as_view(), name='userprofiles'),
    path('userprofiles/add', views.UserCreate.as_view(), name='usercreate'),
    path('userprofiles/<pk>', views.UserDetail.as_view(), name='userdetail'),
]
