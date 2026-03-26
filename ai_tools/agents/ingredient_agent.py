import anthropic
import json
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def run_ingredient_story(ingredient_name):
    prompt = f"""You are a nutrition expert writing for Luca — a premium Indian nut butter brand.

Tell the story of this ingredient: {ingredient_name}

Return ONLY a valid JSON object with these fields:
headline, story, benefits (array of 4 items), fun_fact.
No markdown, no backticks, no extra text. Pure JSON only."""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=600,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "{"}
        ]
    )

    response_text = "{" + message.content[0].text.strip()
    return json.loads(response_text)
