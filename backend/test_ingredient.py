import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import anthropic
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=600,
    messages=[{"role": "user", "content": 'Tell me about Almonds in JSON format with fields: headline, story, benefits array, fun_fact. Return ONLY JSON.'}]
)

print("RAW RESPONSE:")
print(repr(message.content[0].text))
