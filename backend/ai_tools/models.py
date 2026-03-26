from django.db import models


class AgentQuery(models.Model):
    AGENT_CHOICES = [
        ('nutrition_decoder', 'Nutrition Decoder'),
        ('ingredient_story', 'Ingredient Story'),
        ('recipe_breakdown', 'Recipe Breakdown'),
    ]

    agent = models.CharField(max_length=50, choices=AGENT_CHOICES)
    input_text = models.TextField()
    output_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    error_message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_agent_display()} — {self.created_at.strftime('%d %b %Y %H:%M')}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Agent Query'
        verbose_name_plural = 'Agent Queries'