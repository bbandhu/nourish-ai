from django.contrib import admin
from .models import AgentQuery

@admin.register(AgentQuery)
class AgentQueryAdmin(admin.ModelAdmin):
    list_display = ['agent', 'input_text', 'success', 'created_at']
    list_filter = ['agent', 'success']
    readonly_fields = ['created_at']
