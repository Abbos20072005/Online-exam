from django.urls import path

from .serializers import ExamSerializer
from .views import SubjectViewSet, QuestionViewSet, AnswerViewSet, ParticipantViewSet, ExamViewSet

urlpatterns = [
    path('create/subject/', SubjectViewSet.as_view({'post': 'create_subject'}), name='create_subject'),
    path('subject/<int:pk>/', SubjectViewSet.as_view({'patch': 'update_subject', 'delete': 'delete_subject'}), name='subject_action'),
    path('subject/', SubjectViewSet.as_view({'get': 'list_subjects'}), name='list_subjects'),
    path('create/question/', QuestionViewSet.as_view({'post': 'create_question'}), name='create_question'),
    path('question/<int:pk>/', QuestionViewSet.as_view({'patch': 'update_question', 'delete': 'delete_question'}), name='question_action'),
    path('question/', QuestionViewSet.as_view({'get': 'list_questions'}), name='list_questions'),
    path('create/answer/', AnswerViewSet.as_view({'post': 'create_answer'}), name='create_answer'),
    path('answer/<int:pk>/', AnswerViewSet.as_view({'patch': 'update_answer', 'delete': 'delete_answer'}), name="answer_action"),
    path('answer/', AnswerViewSet.as_view({'get': "list_answer"}), name='list_answers'),
    path('participant/', ParticipantViewSet.as_view({'post': "create_participant"}), name='participant'),
    path('create/exam/', ExamViewSet.as_view({'post': 'create_exam'}), name='create_exam'),
    path('exam/<int:pk>/', ExamViewSet.as_view({'patch': 'update_exam', 'delete': 'delete_exam'}), name="exam_action"),
    path('exam/submit/<int:pk>/', ExamViewSet.as_view({'post': 'submit_answer'}), name='submit_answer')
]