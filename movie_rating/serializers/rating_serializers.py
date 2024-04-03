from rest_framework import serializers
from movie_rating.models import MovieRating


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ('id', 'user', 'movie', 'rating')
