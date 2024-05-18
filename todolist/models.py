from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('datetime',)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("todo_list_app:task-detail", args=[str(self.id)])
