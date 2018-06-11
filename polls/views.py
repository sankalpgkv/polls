from django.shortcuts import render, get_object_or_404
from .models import Question,Choice

def index(request):
    all_questions = Question.objects.all() 
    context={ 'all_questions' : all_questions, }
    return render(request, 'polls/index.html' , context) 

def choices(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/choices.html', { 'question': question })


def selected(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    for choice in question.choice_set.all():
        choice.is_selected=False
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice']) 
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/choices.html', { 
        'question': question,
        'error_message': "You did not select a valid choice.",    
        })
    else:
        selected_choice.is_selected=True
        for choice in question.choice_set.all():
            if choice.id != selected_choice.id:
                choice.is_selected=False
                choice.save()

        selected_choice.votes+=1

        selected_choice.save()
        return render(request , 'polls/choices.html', { 'question' : question })