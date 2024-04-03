from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from movie_rating.models import Movie
from movie_rating.serializers.movie_serializers import (
    MovieSerializer,
    MovieDetailSerializer
)


class MovieCreateAPIView(APIView):
    """
    API View for creating a new movie
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        movie_name = request.data.get('name')
        if Movie.objects.filter(name=movie_name).exists():
            return Response({'error': 'Movie with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing movies, provides the 'read-only' actions like .list() and .retrieve()
    """
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering = ['id']
