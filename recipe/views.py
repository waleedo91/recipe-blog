from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import RecipeSerializer, RecipeImageSerializer
from .models import Recipe

# Create your views here.


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    authentication_classes = [SessionAuthentication]
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeSerializer
        elif self.action == 'upload_image':
            return RecipeImageSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        self.http_method_names.append('GET')
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
