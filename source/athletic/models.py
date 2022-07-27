from django.db import models

class Athletic(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    initials = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=60)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.initials