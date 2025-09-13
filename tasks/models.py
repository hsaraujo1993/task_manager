import uuid

from django.contrib.auth.models import User
from django.db import models

from tags.models import Tag

# Create your models here.

STATUS_CHOICES = (
    ("todo", "A fazer"),
    ("doing", "Em andamento"),
    ("done", "Concluído"),
)

PRIORITY_CHOICES = (
    ('low', 'Baixa'),
    ('medium', 'Media'),
    ('high', 'Alta')
)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks', null=False)

    def __str__(self):
        return self.title
