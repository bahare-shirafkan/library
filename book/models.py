from django.db import models
from django.utils import timezone


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='city',
                             on_delete=models.CASCADE)


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    shabak = models.CharField(max_length=20, null=True)
    price = models.IntegerField(null=True)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    cities = models.ManyToManyField(City)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def clean(self):
        if self.published_date and self.published_date > timezone.now().date():
            raise ValueError("Published date cannot be in the future")
        if not self.authors.exists():
            raise ValueError("At least one author is required.")
        if not self.genres.exists():
            raise ValueError("At least one genre is required.")
