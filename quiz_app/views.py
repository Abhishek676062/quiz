from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Quiz
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def create_quiz(request):
    # Handle the POST request to create a new quiz
    if request.method == 'POST':
        question = request.POST.get('question')
        options = request.POST.getlist('options[]')
        right_answer = int(request.POST.get('rightAnswer'))
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        # Create a new quiz object and save it to the database
        quiz = Quiz(question=question, options=options, right_answer=right_answer,
                    start_date=start_date, end_date=end_date)
        quiz.save()

        return JsonResponse({'message': 'Quiz created successfully'})

def get_active_quiz(request):
    # Retrieve the active quiz
    active_quiz = Quiz.objects.filter(status='active').first()

    if active_quiz:
        return JsonResponse({
            'question': active_quiz.question,
            'options': active_quiz.options,
            'rightAnswer': active_quiz.right_answer,
            'startDate': active_quiz.start_date,
            'endDate': active_quiz.end_date
        })
    else:
        return JsonResponse({'message': 'No active quiz found'})

def get_quiz_result(request, quiz_id):
    # Retrieve the quiz result by quiz ID
    try:
        quiz = Quiz.objects.get(id=quiz_id)
        return JsonResponse({'result': quiz.right_answer})
    except Quiz.DoesNotExist:
        return JsonResponse({'message': 'Quiz not found'})

def get_all_quizzes(request):
    # Retrieve all quizzes
    quizzes = Quiz.objects.all()
    quiz_list = []
    for quiz in quizzes:
        quiz_list.append({
            'id': quiz.id,
            'status': quiz.status,
            'question': quiz.question,
            'options': quiz.options,
            'rightAnswer': quiz.right_answer,
            'startDate': quiz.start_date,
            'endDate': quiz.end_date
        })

    return JsonResponse(quiz_list, safe=False)