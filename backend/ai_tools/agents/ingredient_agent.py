import anthropic
import json
import re
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def run_ingredient_story(ingredient_name):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=600,
        messages=[
            {"role": "user", "content": f"Return a JSON object about this ingredient for Luca nut butter brand: {ingredient_name}. Fields: headline (string), story (string, 2-3 sentences), benefits (array of 4 strings), fun_fact (string). JSON only, no other text."}
        ]
    )
    response_text = message.content[0].text.strip()
    match = re.search(r"\{.*\}", response_text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError(f"No JSON found in response: {response_text}")
