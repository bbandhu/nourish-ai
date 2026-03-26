from rest_framework import generics
from .models import Ingredient
from .serializers import IngredientSerializer

class IngredientListView(generics.ListAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

class IngredientDetailView(generics.RetrieveAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    lookup_field = 'slug'
