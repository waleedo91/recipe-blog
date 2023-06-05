import os
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

def upload_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    description = models.TextField(null=True, blank=True)
    prep_time = models.IntegerField(_('Prep Time'))
    cook_time = models.IntegerField(_('Cook Time'))
    date_created = models.DateField(_('Created'), auto_now_add=True)
    image = models.ImageField(null=True, upload_to=upload_image_path)

    def __str__(self):
        return self.title
