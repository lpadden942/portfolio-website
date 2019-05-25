from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField()
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(blank=True, null=True)
