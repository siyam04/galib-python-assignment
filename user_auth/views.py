from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.filters import OrderingFilter
from django.contrib.auth import authenticate, logout
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer


CustomUser = get_user_model()


class UserCreateAPIView(APIView):
    """
    API View for creating a new user
    """
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing users, provides the 'read-only' actions like .list() and .retrieve()
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['phone']
    ordering = ['id']


class UserAuthAPIView(APIView):
    """
    API View for simple login & logout. Token based authentication will be good.
    This login & logout won't make any changes to the user without sending token to API headers.
    """

    # Login request
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

    # Logout request
    def get(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
