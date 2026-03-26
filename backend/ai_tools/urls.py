from django.urls import path
from . import views

urlpatterns = [
    path('nutrition-decoder/', views.NutritionDecoderView.as_view(), name='nutrition-decoder'),
    path('ingredient-story/', views.IngredientStoryView.as_view(), name='ingredient-story'),
    path('recipe-breakdown/', views.RecipeBreakdownView.as_view(), name='recipe-breakdown'),
]
