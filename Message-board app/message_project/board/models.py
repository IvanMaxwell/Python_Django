from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=50)                              # Name of the user
    content = models.TextField()                                         # The actual message
    timestamp = models.DateTimeField(auto_now_add=True)                # Auto-added time

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"                     # First 20 chars as preview
