from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    type = models.CharField(default="REVIEW", editable=False, max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, db_index=True)
    ip = models.GenericIPAddressField(null=True, editable=False)
    location = models.TextField()
    attachedPhotoIds = models.ImageField(upload_to='uploads/', blank=True)
    point = models.IntegerField(default=0, editable=False)