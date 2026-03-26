import anthropic
import json
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def run_recipe_breakdown(recipe_name, ingredients):
    prompt = f"""You are a nutrition expert. Calculate the nutrition breakdown for this recipe.

Recipe: {recipe_name}

Ingredients:
{chr(10).join(f'- {i}' for i in ingredients)}

Assume 4 servings unless specified.

Return ONLY a valid JSON object with exactly these fields:
{{
    "per_serving": {{
        "calories": <number>,
        "protein": <number in grams>,
        "fat": <number in grams>,
        "carbs": <number in grams>,
        "fibre": <number in grams>
    }},
    "servings": <number>,
    "meal_prep_tip": "<one practical meal prep tip>",
    "best_for": "<who this recipe is best for>"
}}

No extra text. Just the JSON."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(message.content[0].text.strip())
