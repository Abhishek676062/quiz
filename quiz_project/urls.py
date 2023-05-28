from django.urls import path

from quiz_app import views
from quiz_app.views import index, create_quiz, get_active_quiz, get_quiz_result, get_all_quizzes


app_name = 'quiz_app'

urlpatterns = [
    path('', index, name='index'),
    path('quizzes/', create_quiz, name='create_quiz'),
    path('quizzes/active/', get_active_quiz, name='get_active_quiz'),
    path('quizzes/<int:quiz_id>/result/', get_quiz_result, name='get_quiz_result'),
    path('quizzes/all/', get_all_quizzes, name='get_all_quizzes'),
]