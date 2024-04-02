from django.urls import path
from rest_framework.routers import DefaultRouter


app_name = 'user_auth'
router = DefaultRouter()


urlpatterns = []

# Included routers
urlpatterns += router.urls
