from django.contrib import admin
from .models import Recipe, RecipeStep, RecipeIngredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'audience', 'prep_time_mins', 'calories_per_serving']
    list_filter = ['audience']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'order', 'instruction']

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'name', 'quantity']
