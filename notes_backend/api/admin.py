from django.contrib import admin
from .models import Note

# Register Note for admin interface (useful for local/admin management).
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-updated_at',)
