from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from movie_rating.models import MovieRating
from movie_rating.serializers.rating_serializers import MovieRatingSerializer


class RateMovieAPIView(APIView):
    """
    API View for rating a movie
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MovieRatingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingListAPIView(generics.ListAPIView):
    """
    ListAPI View for listing movie ratings
    """
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer
