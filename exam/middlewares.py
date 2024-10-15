from django.http import JsonResponse
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from utils.check_token import get_role
from .views import SubjectViewSet, QuestionViewSet, AnswerViewSet


class LeadDetailRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        student_id = view_kwargs.get('pk')
        if student_id is None:
            return None
        target_urls = reverse(viewname='detail_admin', kwargs={'pk': student_id})
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1, 2]:
                return (request,
                        *view_args,
                        ** view_kwargs)
            if role in [4]:
                return (request,
                        *view_args,
                        ** view_kwargs)
            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


class SubjectCreateRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        target_urls = [reverse('create_subject')]
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1]:
                return SubjectViewSet.as_view({'post': 'create_subject'})(request, *view_args, **view_kwargs)
            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


class SubjectActionRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        subject_id = view_kwargs.get('pk')
        if subject_id is None:
            return None
        target_urls = reverse(viewname='subject_action', kwargs={'pk': subject_id})
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1]:
                return SubjectViewSet.as_view({'patch': 'update_subject', 'delete': 'delete_subject'})(request,
                                                                                                       *view_args,
                                                                                                       **view_kwargs)

            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


class QuestionCreateRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        target_urls = [reverse('create_question')]
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1]:
                return QuestionViewSet.as_view({'post': 'create_question'})(request, *view_args, **view_kwargs)
            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


class QuestionActionRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        question_id = view_kwargs.get('pk')
        if question_id is None:
            return None
        target_urls = reverse(viewname='subject_action', kwargs={'pk': question_id})
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1]:
                return SubjectViewSet.as_view({'patch': 'update_question', 'delete': 'delete_question'})(request,
                                                                                                       *view_args,
                                                                                                       **view_kwargs)

            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


class AnswerCreateRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        target_urls = [reverse('create_answer')]
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1]:
                return AnswerViewSet.as_view({'post': 'create_answer'})(request, *view_args, **view_kwargs)
            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


class AnswerActionRoleBasedRedirectMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        answer_id = view_kwargs.get('pk')
        if answer_id is None:
            return None
        target_urls = reverse(viewname='answer_action', kwargs={'pk': answer_id})
        if request.path in target_urls:
            role = get_role(request.headers.get('Authorization'))

            if role in [1]:
                return SubjectViewSet.as_view({'patch': 'update_answer', 'delete': 'delete_answer'})(request,
                                                                                                       *view_args,
                                                                                                       **view_kwargs)

            return JsonResponse(data={"result": "", "error": "Permission denied", 'ok': False}, status=403)
        return None


