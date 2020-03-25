from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
