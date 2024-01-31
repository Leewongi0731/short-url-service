from django.db import models


# Create your models here.
class ShortUrl(models.Model):
    id = models.UUIDField(primary_key=True)
    short_url = models.CharField(max_length=20, unique=True, db_index=True)
    original_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
