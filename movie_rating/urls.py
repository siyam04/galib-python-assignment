from django.urls import path
from rest_framework.routers import DefaultRouter


app_name = 'movie_rating'
router = DefaultRouter()


urlpatterns = []

# Included routers
urlpatterns += router.urls
