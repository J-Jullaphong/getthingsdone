import uuid
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def todo_image_upload_path(instance, filename):
    """Return the upload path for the todo item's image based on its UUID."""
    extension = filename.split('.')[-1]
    return f'todo_images/{instance.id}.{extension}'


class Todo(models.Model):
    """This model represents a todo item in the application."""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    image = models.ImageField(upload_to=todo_image_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.status}"

    def clean(self):
        """Ensure the due date is not set in the past."""
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError("Due date cannot be in the past.")

    @property
    def is_overdue(self):
        """
        Checks if the todo item is overdue.
        A task is considered overdue if its due date is in the past and its status is not 'DONE'.
        """
        return self.due_date and self.due_date < timezone.now() and self.status != 'DONE'

