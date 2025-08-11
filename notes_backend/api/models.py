from django.db import models

# PUBLIC_INTERFACE
class Note(models.Model):
    """A simple Note model for storing user notes."""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when note was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when note was last updated")

    def __str__(self):
        return self.title
