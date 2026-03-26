from django.db import models
from products.models import Product

class Recipe(models.Model):
    AUDIENCE_CHOICES = [
        ('kids', 'Kids'),
        ('athlete', 'Athlete'),
        ('everyday', 'Everyday'),
        ('traditional', 'Traditional'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='recipes/', blank=True)
    audience = models.CharField(max_length=20, choices=AUDIENCE_CHOICES, default='everyday')
    prep_time_mins = models.IntegerField(default=10)
    calories_per_serving = models.IntegerField(null=True, blank=True)
    protein_per_serving = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    products_used = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    order = models.IntegerField()
    instruction = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.recipe.title} — Step {self.order}"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} {self.name}"