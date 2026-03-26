import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from ingredients.models import Ingredient, IngredientBenefit, IngredientNutrition

Ingredient.objects.all().delete()
print("Cleared existing ingredients...")

ingredients_data = [
    {
        'name': 'Roasted Peanuts',
        'slug': 'roasted-peanuts',
        'benefits': [
            'High protein — 25g per 100g',
            'Heart-healthy monounsaturated fats',
            'Rich in Vitamin E',
            'Natural source of resveratrol',
            'Supports muscle recovery',
        ],
        'nutrition': {
            'calories': 588, 'protein': 25.0,
            'fat': 50.0, 'carbs': 20.0, 'fibre': 8.0,
        }
    },
    {
        'name': 'Raw Almonds',
        'slug': 'raw-almonds',
        'benefits': [
            'Rich in Vitamin E — powerful antioxidant',
            'High in magnesium for muscle recovery',
            'Supports bone health with calcium',
            'Low glycemic index — steady energy',
            'Heart-healthy fats',
        ],
        'nutrition': {
            'calories': 614, 'protein': 21.0,
            'fat': 56.0, 'carbs': 19.0, 'fibre': 12.0,
        }
    },
    {
        'name': 'Cashews',
        'slug': 'cashews',
        'benefits': [
            'Rich in iron for sustained energy',
            'High zinc for immune support',
            'Copper for healthy skin and hair',
            'Naturally creamy — no oil needed',
            'Brain-boosting healthy fats',
        ],
        'nutrition': {
            'calories': 553, 'protein': 18.0,
            'fat': 44.0, 'carbs': 30.0, 'fibre': 3.0,
        }
    },
    {
        'name': 'Pistachios',
        'slug': 'pistachios',
        'benefits': [
            'Highest protein nut — 20g per 100g',
            'Rich in Vitamin B6 for brain health',
            'Lutein and zeaxanthin for eye health',
            'Potassium for heart health',
            'Rich in antioxidants',
        ],
        'nutrition': {
            'calories': 560, 'protein': 20.0,
            'fat': 45.0, 'carbs': 28.0, 'fibre': 10.0,
        }
    },
    {
        'name': 'Dark Chocolate',
        'slug': 'dark-chocolate',
        'benefits': [
            'Rich in flavanoids and antioxidants',
            'Supports heart health',
            'Mood-boosting compounds',
            'No milk solids — dairy free',
            'No refined sugar added',
        ],
        'nutrition': {
            'calories': 546, 'protein': 5.0,
            'fat': 31.0, 'carbs': 60.0, 'fibre': 7.0,
        }
    },
    {
        'name': 'Himalayan Pink Salt',
        'slug': 'himalayan-pink-salt',
        'benefits': [
            '84 trace minerals',
            'Natural electrolyte',
            'Supports hydration',
            'Minimally processed',
            'Enhances natural flavours',
        ],
        'nutrition': {
            'calories': 0, 'protein': 0.0,
            'fat': 0.0, 'carbs': 0.0, 'fibre': 0.0,
        }
    },
    {
        'name': 'Rolled Oats',
        'slug': 'rolled-oats',
        'benefits': [
            'Slow-release carbohydrates',
            'High in beta-glucan fibre',
            'Supports gut health',
            'Gluten free',
            'Keeps you full longer',
        ],
        'nutrition': {
            'calories': 389, 'protein': 17.0,
            'fat': 7.0, 'carbs': 66.0, 'fibre': 11.0,
        }
    },
    {
        'name': 'Medjool Dates',
        'slug': 'medjool-dates',
        'benefits': [
            'Natural sweetener — no refined sugar',
            'High in fibre for gut health',
            'Rich in potassium for heart health',
            'Natural energy boost',
            'Contains iron and magnesium',
        ],
        'nutrition': {
            'calories': 277, 'protein': 2.0,
            'fat': 0.2, 'carbs': 75.0, 'fibre': 7.0,
        }
    },
    {
        'name': 'Raw Cocoa',
        'slug': 'raw-cocoa',
        'benefits': [
            'Highest antioxidant food on earth',
            'Rich in magnesium for energy',
            'Mood-boosting theobromine',
            'Supports heart health',
            'Iron-rich for energy production',
        ],
        'nutrition': {
            'calories': 228, 'protein': 20.0,
            'fat': 14.0, 'carbs': 58.0, 'fibre': 33.0,
        }
    },
]

for data in ingredients_data:
    benefits = data.pop('benefits')
    nutrition = data.pop('nutrition')

    ingredient = Ingredient.objects.create(**data)

    for benefit in benefits:
        IngredientBenefit.objects.create(
            ingredient=ingredient,
            benefit=benefit
        )

    IngredientNutrition.objects.create(
        ingredient=ingredient,
        **nutrition
    )

    print(f"✅ {ingredient.name}")

print("\n🎉 All ingredients seeded!")
