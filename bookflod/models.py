from django.db import models
from django.contrib.auth.models import User

#Country Model, meant to hold
# - name
class Country(models.Model) :
    name = models.CharField(
        max_length = 100)

    def __str__(self):
        return self.name

    class Meta(object) :
        verbose_name_plural = 'Countries'

class Language(models.Model) :
    name = models.CharField(
        max_length = 100)

    def __str__(self):
        return self.name

class Genre(models.Model) :
    name = models.CharField(
        max_length = 100)

    def __str__(self):
        return self.name

class Book(models.Model) :
    title = models.CharField(
        max_length = 255)
    author = models.CharField(
        max_length = 255)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)
    isbn = models.IntegerField(
        blank = True,
        null = True,
    )
    date_published = models.DateField(blank = True, null = True)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class UserProfile(models.Model) :
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    dob = models.DateField()
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    books_read = models.ManyToManyField(Book, related_name = 'read_it')
    books_wanted = models.ManyToManyField(Book, related_name = 'want_it')
    genre = models.ManyToManyField(Genre)
    langugaes = models.ManyToManyField(Language)


    def __str__(self):
        return self.user.get_full_name()
