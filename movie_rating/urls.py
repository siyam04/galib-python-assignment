from django.urls import path
from rest_framework.routers import DefaultRouter

from movie_rating.views.movie_views import (
    MovieCreateAPIView,
    MovieReadOnlyModelViewSet
)

from movie_rating.views.rating_views import (
    RateMovieAPIView,
    RatingListAPIView
)


app_name = 'movie_rating'
router = DefaultRouter()


# Movie List: /api/v1/movies/
# Movie Details: /api/v1/movies/{id}/
router.register(r"movies", MovieReadOnlyModelViewSet)


urlpatterns = [

    # Create movie: /api/v1/create-movie/
    path('create-movie/', MovieCreateAPIView.as_view(), name='create-movie'),

    # Rate movie: /api/v1/rate-movie/
    path('rate-movie/', RateMovieAPIView.as_view(), name='rate-movie'),

    # Rating List: /api/v1/ratings/
    path('ratings/', RatingListAPIView.as_view(), name='ratings'),
]

# Included routers
urlpatterns += router.urls
