from rest_framework import serializers
from .models import Ingredient, IngredientBenefit, IngredientNutrition

class IngredientBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientBenefit
        fields = ['id', 'benefit']

class IngredientNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientNutrition
        fields = ['id', 'calories', 'protein', 'fat', 'carbs', 'fibre', 'per_grams']

class IngredientSerializer(serializers.ModelSerializer):
    benefits = IngredientBenefitSerializer(many=True)
    nutrition = IngredientNutritionSerializer(many=True)

    class Meta:
        model = Ingredient
        fields = [
            'id', 'name', 'slug', 'description',
            'image', 'sourced_from', 'benefits', 'nutrition'
        ]
