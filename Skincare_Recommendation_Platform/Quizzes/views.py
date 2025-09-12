from django.shortcuts import render, redirect
from .models import QuizResults, Question
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import QuizForm
from django.contrib.auth.decorators import login_required

from .models import Question
# Create your views here.
@login_required
def QuizPage(request):
    questions = Question.objects.all().order_by('order')
    answers = {}
    empty = False
    if(request.method == 'POST'):
        for question in questions:
            key = f'question_{question.id}' # type: ignore
            if(question.type == 'multiple_choice'):
                answer = request.POST.getlist(key)
            elif(question.type == 'single_choice'):
                answer = request.POST.get(key)
            else:
                answer = request.POST.get(key)
            answers[question.id] = answer # type: ignore
        for key, value in answers.items():
            if(value == []):
                empty = True
        if( empty == False ):
            if(QuizResults.objects.filter(user=request.user).exists()):
                QuizResults.objects.filter(user=request.user).delete()
            QuizResults.objects.create(user=request.user, skin_type=answers[2], concerns=answers[4], eye_concern=answers[8], budget=answers[7], age=answers[3], preferences=answers[5], dryness=int(answers[9]))
            return redirect('/routines')

    question_ids = [question.id for question in questions] # type: ignore

    return render(request, 'Quizzes/quiz_page.html', {'questions': questions, 'question_ids':question_ids, 'empty': empty})