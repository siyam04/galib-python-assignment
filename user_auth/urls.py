from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    UserCreateAPIView,
    UserReadOnlyModelViewSet,
    UserAuthAPIView
)


app_name = 'user_auth'
router = DefaultRouter()


# User List: /api/v1/auth/users/
# User Details: /api/v1/auth/users/{id}/
router.register(r"users", UserReadOnlyModelViewSet)


urlpatterns = [

    # Create user: /api/v1/auth/create-user/
    path('create-user/', UserCreateAPIView.as_view(), name='create-user'),

    # Login user: /api/v1/auth/login/
    path('login/', UserAuthAPIView.as_view(), name='login'),

    # Logout user: /api/v1/auth/logout/
    path('logout/', UserAuthAPIView.as_view(), name='logout'),

]

# Included routers
urlpatterns += router.urls
