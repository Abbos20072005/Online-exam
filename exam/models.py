from django.db import models
from authorization.models import User
from abstract_model.base_model import BaseModel
from django.utils import timezone

from exceptions.error_message import ErrorCodes
from exceptions.exception import CustomApiException

QUESTION_TYPE = (
    (1, 'Open'),
    (2, 'Close'),
)


class Exam(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    student_number = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def in_process(self):
        now = timezone.now()
        return self.start_date <= now <= self.end_date


class Participant(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    question = models.CharField(max_length=500)
    type = models.PositiveIntegerField(choices=QUESTION_TYPE, default=1)
    correct_option = models.ForeignKey("Option", null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name='correctly_answered_questions')

    def __str__(self):
        return self.subject.name

    def clean(self):
        if self.type == 2 and not self.correct_option:
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT,
                                     message="Closed questions must have a correct option.")


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_options')
    text = models.CharField(max_length=255)


class Answers(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question.name


class UserAnswer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.SET_NULL)
    open_answer = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.question.type == 2:
            self.is_correct = self.selected_option == self.question.correct_option
        super().save(*args, **kwargs)
