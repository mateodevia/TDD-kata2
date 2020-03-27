from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Portafolio(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)

