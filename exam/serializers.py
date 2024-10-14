from .models import Subject, Question, Answers
from rest_framework import serializers


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
