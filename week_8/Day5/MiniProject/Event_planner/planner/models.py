from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ResourceList(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

