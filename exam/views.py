from exceptions.error_message import ErrorCodes
from exceptions.exception import CustomApiException
from .models import Subject, Question, Answers, Exam, Participant
from .serializers import SubjectSerializer, QuestionSerializer, AnswerSerializer, ExamSerializer, ParticipantSerializer
from rest_framework.viewsets import ViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status

class ExamViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create exam',
        operation_description='Create Exam',
        request_body=ExamSerializer(),
        responses={201: ExamSerializer()},
        tags=['Exam']
    )
    def create_exam(self, request):
        data = request.data
        serializer = ExamSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)


class ParticipantViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create participant',
        operation_description='Create participant',
        request_body=ParticipantSerializer(),
        responses={201: ParticipantSerializer()},
        tags=['Participant']
    )
    def create_participant(self, request):
        data = request.data
        serializer = ParticipantSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        exam_id = serializer.validated_data.get('exam')
        participant = Participant.objects.filter(exam_id=exam_id).count()
        exam = Exam.objects.filter(id=exam_id).first()
        if participant >= exam.student_number:
            raise CustomApiException(error_code=ErrorCodes.INVALID_INPUT, message="Exam participants reach the maximum value")

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

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
        operation_summary='List of subjects',
        operation_description='List of subjects',
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
        operation_description='Delete question, pk receive question id',
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
        operation_summary='List of questions',
        operation_description='List of questions',
        responses={200: QuestionSerializer()},
        tags=['Question']
    )
    def list_questions(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)


class AnswerViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create answer',
        operation_description='Create answer',
        request_body=AnswerSerializer(),
        responses={201: AnswerSerializer()},
        tags=['Answer']
    )
    def create_answer(self, request):
        data = request.data
        serializer = AnswerSerializer(data=data, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='Update answer, pk receive answer id',
        operation_description='Update answer, pk receive answer id',
        request_body=AnswerSerializer(),
        responses={200: AnswerSerializer()},
        tags=['Answer']
    )
    def update_answer(self, request, pk):
        data = request.data
        answer = Answers.obejcts.filter(id=pk, question__subject__user_id=request.user.id).first()
        if not answer:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        serializer = AnswerSerializer(answer, data=data, partial=True, context={'request': request})
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Delete answer, pk receive answer id',
        operation_description='Delete answer, pk receive answer id',
        responses={204: AnswerSerializer()},
        tags=['Answer']
    )
    def delete_answer(self, request, pk):
        answer = Answers.objects.filter(id=pk, question__subject__user_id=request.user.id).first()
        if not answer:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)

        answer.delete()
        return Response(data={'result': "Answer successfully deleted", 'ok': True}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='List of answers',
        operation_description='List of answers',
        responses={200: QuestionSerializer()},
        tags=['Question']
    )
    def list_answers(self, request):
        answers = Answers.objects.all()
        serializer = QuestionSerializer(answers, many=True, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)