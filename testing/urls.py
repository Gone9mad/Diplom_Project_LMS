from django.urls import path

from testing.apps import TestingConfig
from testing.views import QuestionListAPIView, QuestionDetailAPIView, SendAnswerApiView

app_name = TestingConfig.name


urlpatterns = [
    path('questions/list/', QuestionListAPIView.as_view(), name='questions_list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question_detail'),
    path('questions/<int:question_id>/send_answer/', SendAnswerApiView.as_view(), name='send_answer'),  # This endpoint sends an answer to a question.
]
