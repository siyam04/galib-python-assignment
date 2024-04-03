from django.contrib import admin
from .models import Movie, MovieRating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'rating', 'release_date']
    list_display_links = ['name']
    ordering = ['id']


@admin.register(MovieRating)
class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'rating']
    list_display_links = ['id']
    ordering = ['id']
