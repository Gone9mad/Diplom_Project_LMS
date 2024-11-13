from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from testing.models import Question, Answers
from testing.serializers import (QuestionListSerializer, QuestionRetrieveSerializer,
                                 SendAnswerRequest, SendAnswerResponse)
from users.permissions import IsStudents


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = (IsAuthenticated | IsStudents, ) #(AllowAny,)


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionRetrieveSerializer
    permission_classes = (IsAuthenticated | IsStudents, ) #(AllowAny,)


class SendAnswerApiView(APIView):
    permission_classes = (IsAuthenticated, ) #(AllowAny,)

    def post(self, request, question_id, **kwargs):
        serializer = SendAnswerRequest(data=request.data)
        serializer.is_valid()
        answer: list[int] = serializer.validated_data['answers']
        question = get_object_or_404(Question, pk=question_id)
        answers = question.answers_set.all()
        correct_answers_ids = answers.filter(is_correct=True).values_list('id', flat=True)

        if set(answer) == set(correct_answers_ids):
            serializer = SendAnswerResponse(answers, many=True)
            return Response(serializer.data, status=200)

        return Response({'code': 'Invalid'}, status=400)
