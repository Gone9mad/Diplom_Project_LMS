from rest_framework import serializers
from rest_framework.fields import IntegerField

from testing.models import Question, Answers


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SendAnswerResponse(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'is_correct')


class SendAnswerRequest(serializers.Serializer):
    answers = serializers.ListField(children=IntegerField())

