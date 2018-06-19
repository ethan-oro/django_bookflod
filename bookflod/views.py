from django.shortcuts import render
from bookflod.models import UserProfile
#series of funciton / classea that take data and display them on the page


def home(request) :
    user_profiles = UserProfile.objects.all()
    data = { 'people' : user_profiles }
    return render(request, 'home.html', data)
