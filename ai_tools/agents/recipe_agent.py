import anthropic
import json
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def run_recipe_breakdown(recipe_name, ingredients):
    prompt = f"""You are a nutrition expert. Calculate nutrition for this recipe.

Recipe: {recipe_name}
Ingredients: {', '.join(ingredients)}

Return ONLY this exact JSON structure with no other text:
{{"per_serving": {{"calories": 300, "protein": 10, "fat": 12, "carbs": 40, "fibre": 5}}, "servings": 4, "meal_prep_tip": "Make ahead and store in fridge.", "best_for": "Athletes and active people"}}

Replace values with accurate nutrition for the given recipe. Return ONLY the JSON."""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text.strip()

    # Clean any markdown
    if '```' in response_text:
        response_text = response_text.split('```')[1]
        if response_text.startswith('json'):
            response_text = response_text[4:].strip()

    # Find JSON object
    start = response_text.find('{')
    end = response_text.rfind('}') + 1
    if start != -1 and end > start:
        response_text = response_text[start:end]

    return json.loads(response_text)
