from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=15, null=True, blank=True)

    
    def __str__(self):
        return self.title