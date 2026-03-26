import anthropic
import json
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def run_nutrition_decoder(ingredients: list[str]) -> dict:
    prompt = f"""You are a nutrition expert. Calculate the nutrition facts for the following ingredients combined.

Ingredients:
{chr(10).join(f'- {i}' for i in ingredients)}

Return ONLY a valid JSON object with exactly these fields:
{{
    "calories": <number per 100g>,
    "protein": <number in grams>,
    "fat": <number in grams>,
    "carbs": <number in grams>,
    "fibre": <number in grams>,
    "summary": "<one sentence about this combination>"
}}

No extra text. Just the JSON."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text.strip()
    return json.loads(response_text)
