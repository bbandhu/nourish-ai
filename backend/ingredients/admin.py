from django.contrib import admin
from .models import Ingredient, IngredientBenefit, IngredientNutrition

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'sourced_from']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(IngredientBenefit)
class IngredientBenefitAdmin(admin.ModelAdmin):
    list_display = ['ingredient', 'benefit']

@admin.register(IngredientNutrition)
class IngredientNutritionAdmin(admin.ModelAdmin):
    list_display = ['ingredient', 'calories', 'protein', 'fat', 'carbs', 'fibre']
