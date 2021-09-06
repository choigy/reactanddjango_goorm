from django.db import models
from django.utils import timezone

class Test(models.Model):
    name=models.CharField(max_length=200)
    nidk=models.CharField(max_length=200)
    created=models.DateTimeField(timezone.now())

# Create your models here.
