from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


CustomUser = get_user_model()


class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class MovieRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], max_digits=3, decimal_places=1)

    class Meta:
        unique_together = ('user', 'movie')  # Ensure a user can only rate a movie once

    def __str__(self):
        return f"{self.user.username}'s rating for {self.movie.name}: {self.rating}"
