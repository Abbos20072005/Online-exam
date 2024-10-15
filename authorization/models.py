from django.db import models

USER_ROLE = (
    (1, 'Teacher'),
    (2, 'Student'),
)

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=40)
    role = models.PositiveIntegerField(choices=USER_ROLE, default=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username