from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        audience = self.request.query_params.get('audience')
        if audience:
            queryset = queryset.filter(audience=audience)
        return queryset

class RecipeDetailView(generics.RetrieveAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = 'slug'
