from django.contrib.auth.models import User
from django.db import models


class ResourceList(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


# author = models.ForeignKey(User, on_delete=models.CASCADE)
