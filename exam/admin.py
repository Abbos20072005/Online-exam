from django.contrib import admin
from .models import Exam, Subject, Question, Answers, UserAnswer, Option

admin.site.register(Exam)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(UserAnswer)
admin.site.register(Option)