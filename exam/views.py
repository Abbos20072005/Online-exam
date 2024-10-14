from exceptions.error_message import ErrorCodes
from exceptions.exception import CustomApiException
from .models import Subject, Question, Answers
from .serializers import SubjectSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status


class SubjectViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create subject',
        operation_description='Create subject',
        request_body=SubjectSerializer(),
        responses={201: SubjectSerializer()},
        tags=['Subject']
    )
    def create_subject(self, request):
        data = request.data
        serializer = SubjectSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Update subject, pk receive subject id',
        operation_description='Update subject, pk receive subject id',
        request_body=SubjectSerializer(),
        responses={200: SubjectSerializer()},
        tags=['Subject']
    )
    def update_subject(self, request, pk):
        data = request.data
        subject = Subject.obejcts.filter(id=pk, user_id=request.user.id).first()
        if not subject:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = SubjectSerializer(subject, data=data, partial=True, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Delete subject, pk receive subject id',
        operation_description='Delete subject, pk receive subject id',
        responses={204: SubjectSerializer()},
        tags=['Subject']
    )
    def delete_subject(self, request, pk):
        subject = Subject.objects.filter(id=pk, user_id=request.user.id).first()
        if not subject:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        subject.delete()
        return Response(data={'result': "Subject successfully deleted", 'ok': True}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='List of subject',
        operation_description='List of subject',
        responses={200: SubjectSerializer()},
        tags=['Subject']
    )
    def list_subjects(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

class QuestionViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create question',
        operation_description='Create question',
        request_body=QuestionSerializer(),
        responses={201: QuestionSerializer()},
        tags=['Question']
    )
    def create_question(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Update question, pk receive question id',
        operation_description='Update question, pk receive question id',
        request_body=QuestionSerializer(),
        responses={200: QuestionSerializer()},
        tags=['Question']
    )
    def update_question(self, request, pk):
        data = request.data
        question = Question.obejcts.filter(id=pk, subject__user_id=request.user.id).first()
        if not question:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = QuestionSerializer(question, data=data, partial=True, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Delete question, pk receive question id',
        operation_description='Delete subject, pk receive question id',
        responses={204: QuestionSerializer()},
        tags=['Question']
    )
    def delete_question(self, request, pk):
        question = Question.objects.filter(id=pk, subject__user_id=request.user.id).first()
        if not question:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        question.delete()
        return Response(data={'result': "Question successfully deleted", 'ok': True}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='List of question',
        operation_description='List of question',
        responses={200: QuestionSerializer()},
        tags=['Question']
    )
    def list_subjects(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class AnswerViewSet(ViewSet):
    def create_answer(self, request):
        data = request.data
        serializer = AnswerSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)