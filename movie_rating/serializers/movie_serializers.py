from django.db.models import Avg
from rest_framework import serializers
from movie_rating.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    release_date = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'rating', 'release_date')
        extra_kwargs = {
            'name': {'required': True},
            'genre': {'required': True},
            'rating': {'required': True},
            'release_date': {'required': True},
        }


class MovieDetailSerializer(serializers.ModelSerializer):
    release_date = serializers.DateField(format="%d-%m-%Y")
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'rating', 'release_date', 'average_rating')

    def get_average_rating(self, obj):
        average_rating = obj.movierating_set.aggregate(Avg('rating'))['rating__avg']
        if average_rating is not None:
            return round(average_rating, 1)  # Round to 1 decimal place
        else:
            return None  # or any other value
