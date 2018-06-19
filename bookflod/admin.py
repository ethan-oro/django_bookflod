from django.contrib import admin
from bookflod.models import Country, Language, Book, UserProfile, Genre

#registering things to the admin?

admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Genre)
