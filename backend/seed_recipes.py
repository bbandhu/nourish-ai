import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from recipes.models import Recipe, RecipeStep, RecipeIngredient

Recipe.objects.all().delete()
print("Cleared existing recipes...")

recipes_data = [
    {
        'title': 'Peanut Butter Banana Pancakes',
        'slug': 'peanut-butter-banana-pancakes',
        'description': 'Fluffy protein-packed pancakes made with Luca Peanut Butter.',
        'audience': 'kids',
        'prep_time_mins': 20,
        'ingredients': [
            ('Luca Peanut Butter', '2 tbsp'),
            ('Ripe banana', '1 large'),
            ('Eggs', '2'),
            ('Oat flour', '1 cup'),
            ('Milk', '½ cup'),
            ('Baking powder', '1 tsp'),
        ],
        'steps': [
            'Mash the banana in a large bowl until smooth.',
            'Add eggs, milk and Luca Peanut Butter. Mix well.',
            'Fold in oat flour and baking powder until just combined.',
            'Heat a non-stick pan over medium heat. Pour ¼ cup batter per pancake.',
            'Cook 2-3 minutes until bubbles form, then flip. Cook 1 more minute.',
            'Serve warm with a drizzle of honey.',
        ]
    },
    {
        'title': 'Pistachio Energy Balls',
        'slug': 'pistachio-energy-balls',
        'description': 'No-bake energy balls with Luca Almond Butter, oats and dates.',
        'audience': 'athlete',
        'prep_time_mins': 10,
        'ingredients': [
            ('Luca Almond Butter', '3 tbsp'),
            ('Medjool dates', '8 pitted'),
            ('Rolled oats', '1 cup'),
            ('Chia seeds', '1 tbsp'),
            ('Pistachios', '¼ cup'),
            ('Himalayan salt', 'a pinch'),
        ],
        'steps': [
            'Blend dates in a food processor until a paste forms.',
            'Add Luca Almond Butter and pulse to combine.',
            'Transfer to a bowl. Add oats, chia seeds and pistachios. Mix well.',
            'Roll into 12 equal balls using your hands.',
            'Refrigerate for 30 minutes to firm up.',
            'Store in fridge for up to 5 days.',
        ]
    },
    {
        'title': 'Almond Butter Protein Shake',
        'slug': 'almond-butter-protein-shake',
        'description': 'A creamy high-protein shake with Luca Almond Butter. Ready in 5 minutes.',
        'audience': 'athlete',
        'prep_time_mins': 5,
        'ingredients': [
            ('Luca Almond Butter', '2 tbsp'),
            ('Frozen banana', '1'),
            ('Oat milk', '1.5 cups'),
            ('Greek yogurt', '½ cup'),
            ('Cocoa powder', '1 tsp'),
            ('Ice cubes', '4-5'),
        ],
        'steps': [
            'Add all ingredients to a blender.',
            'Blend on high for 60 seconds until smooth.',
            'Taste and adjust sweetness with honey if needed.',
            'Pour into a glass and serve immediately.',
        ]
    },
    {
        'title': 'Sattu Peanut Butter Ladoo',
        'slug': 'sattu-peanut-butter-ladoo',
        'description': 'A traditional Indian sweet reimagined with Luca Peanut Butter. No refined sugar.',
        'audience': 'traditional',
        'prep_time_mins': 30,
        'ingredients': [
            ('Luca Peanut Butter', '3 tbsp'),
            ('Sattu flour', '1 cup'),
            ('Jaggery powder', '3 tbsp'),
            ('Ghee', '2 tbsp'),
            ('Cardamom powder', '½ tsp'),
            ('Milk', '2-3 tbsp'),
        ],
        'steps': [
            'Dry roast sattu flour on low heat for 3-4 minutes. Cool completely.',
            'Mix sattu, jaggery, cardamom and Luca Peanut Butter in a bowl.',
            'Add ghee and mix until it resembles breadcrumbs.',
            'Add milk one tablespoon at a time until mixture holds shape.',
            'Roll into 15 equal balls.',
            'Store in airtight container for up to 3 days.',
        ]
    },
    {
        'title': 'Cashew Choco Bark',
        'slug': 'cashew-choco-bark',
        'description': 'Simple 3-ingredient chocolate bark with Luca Cashew Butter. Great for kids.',
        'audience': 'kids',
        'prep_time_mins': 15,
        'ingredients': [
            ('Luca Cashew Butter', '3 tbsp'),
            ('Dark chocolate chips', '1 cup'),
            ('Whole cashews', '¼ cup'),
            ('Himalayan salt', 'a pinch'),
            ('Coconut flakes', '2 tbsp'),
        ],
        'steps': [
            'Melt dark chocolate in a double boiler or microwave.',
            'Pour melted chocolate onto a parchment-lined baking tray.',
            'Drizzle Luca Cashew Butter over the chocolate.',
            'Swirl cashew butter through chocolate with a toothpick.',
            'Scatter cashews, coconut flakes and salt on top.',
            'Refrigerate for 1 hour until set. Break into pieces.',
        ]
    },
    {
        'title': 'Overnight Oats with Peanut Butter',
        'slug': 'overnight-oats-peanut-butter',
        'description': 'No-cook breakfast ready in 5 minutes. Prep the night before.',
        'audience': 'everyday',
        'prep_time_mins': 5,
        'ingredients': [
            ('Luca Peanut Butter', '2 tbsp'),
            ('Rolled oats', '½ cup'),
            ('Oat milk', '½ cup'),
            ('Greek yogurt', '¼ cup'),
            ('Chia seeds', '1 tbsp'),
            ('Honey', '1 tsp'),
        ],
        'steps': [
            'Add oats, chia seeds, milk and yogurt to a jar. Stir well.',
            'Add Luca Peanut Butter and honey. Stir to combine.',
            'Cover and refrigerate overnight or at least 4 hours.',
            'Top with banana slices and extra peanut butter.',
            'Serve cold straight from the jar.',
        ]
    },
]

for recipe_data in recipes_data:
    ingredients = recipe_data.pop('ingredients')
    steps = recipe_data.pop('steps')

    recipe = Recipe.objects.create(**recipe_data)

    for order, instruction in enumerate(steps, start=1):
        RecipeStep.objects.create(
            recipe=recipe,
            order=order,
            instruction=instruction
        )

    for name, quantity in ingredients:
        RecipeIngredient.objects.create(
            recipe=recipe,
            name=name,
            quantity=quantity
        )

    print(f"✅ {recipe.title}")

print("\n🎉 All recipes seeded!")
