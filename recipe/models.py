from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    prep_time = models.IntegerField(_('Prep Time'))
    cook_time = models.IntegerField(_('Cook Time'))
    date_created = models.DateField(_('Created'), auto_now_add=True)

    def __str__(self):
        return self.title
