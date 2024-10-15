from .models import Subject, Question, Answers, Exam, Participant
from rest_framework import serializers

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', "exam", 'full_name', 'phone_number']

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'start_date', 'end_date', 'student_number']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'user', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'subject', 'question', 'type', 'is_active']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'question', 'answer']
