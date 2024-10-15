from django.db import models
from authorization.models import User
from abstract_model.base_model import BaseModel
from django.utils import timezone

QUESTION_TYPE = (
    (1, 'Open'),
    (2, 'Close'),
)


class Exam(BaseModel):
    title = models.CharField(max_length=100)
    student_number = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def in_process(self):
        now = timezone.now()
        return self.start_date <= now <= self.end_date


class Participant(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.full_name


class Subject(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Question(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    question = models.CharField(max_length=500)
    type = models.PositiveIntegerField(choices=QUESTION_TYPE, default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject.name


class Answers(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question.name
