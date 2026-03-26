from rest_framework import serializers
from .models import Recipe, RecipeStep, RecipeIngredient

class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ['id', 'order', 'instruction']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'name', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    steps = RecipeStepSerializer(many=True)
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'slug', 'description',
            'image', 'audience', 'prep_time_mins',
            'calories_per_serving', 'protein_per_serving',
            'steps', 'ingredients'
        ]
