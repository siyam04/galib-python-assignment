from django.contrib import admin
from django.urls import path, include

# drf-yasg (API Documentation)
from utils.swagger_config import schema_view


urlpatterns = [

    # Administration
    path('admin/', admin.site.urls),

    # Api doc (swagger)
    path('', schema_view.with_ui('swagger'), name='schema-swagger-ui'),

    # User auth apis
    path('api/v1/auth/', include('user_auth.urls', namespace='user-auth')),

    # Movie rating apis
    path('api/v1/', include('movie_rating.urls', namespace='movie-rating'))

]
