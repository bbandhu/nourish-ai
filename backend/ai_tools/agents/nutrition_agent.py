import anthropic
import json
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def run_nutrition_decoder(ingredients):
    prompt = f"""You are a nutrition expert. Calculate the nutrition facts for these ingredients combined.

Ingredients:
{chr(10).join(f'- {i}' for i in ingredients)}

Return ONLY a valid JSON object with exactly these fields, no markdown, no backticks, no extra text:
{{
    "calories": 450,
    "protein": 15,
    "fat": 20,
    "carbs": 55,
    "fibre": 8,
    "summary": "A balanced combination of protein and complex carbohydrates."
}}"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    response_text = message.content[0].text.strip()
    if response_text.startswith('```'):
        response_text = response_text.split('```')[1]
        if response_text.startswith('json'):
            response_text = response_text[4:]
    return json.loads(response_text.strip())
