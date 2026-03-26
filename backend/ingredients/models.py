from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ingredients/', blank=True)
    sourced_from = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IngredientBenefit(models.Model):
    ingredient = models.ForeignKey(Ingredient, related_name='benefits', on_delete=models.CASCADE)
    benefit = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ingredient.name} — {self.benefit}"

class IngredientNutrition(models.Model):
    ingredient = models.ForeignKey(Ingredient, related_name='nutrition', on_delete=models.CASCADE)
    calories = models.DecimalField(max_digits=6, decimal_places=1)
    protein = models.DecimalField(max_digits=5, decimal_places=1)
    fat = models.DecimalField(max_digits=5, decimal_places=1)
    carbs = models.DecimalField(max_digits=5, decimal_places=1)
    fibre = models.DecimalField(max_digits=5, decimal_places=1)
    per_grams = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.ingredient.name} — Nutrition per {self.per_grams}g"