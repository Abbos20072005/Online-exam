from django.db import models
from authorization.models import User

QUESTION_TYPE = (
    (1, 'Open'),
    (2, 'Close'),
)

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    question = models.CharField(max_length=500)
    type = models.PositiveIntegerField(choices=QUESTION_TYPE, default=1)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject.name

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question.name
