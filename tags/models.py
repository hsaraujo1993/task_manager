from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tags', null=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
