from django.db import models

from tags.models import Tag
from tasks.models import Task


# Create your models here.


class TaskTag(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['task', 'tag'], name='unique_task_tag')
        ]


