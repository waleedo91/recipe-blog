from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import RecipeSerializer
from .models import Recipe

# Create your views here.


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    authentication_classes = [SessionAuthentication]
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
