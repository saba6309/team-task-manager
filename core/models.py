from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Member', 'Member'),
)

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
)

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title