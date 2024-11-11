from django.contrib import admin

from testing.models import Question, Answers


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answers', 'is_correct')
