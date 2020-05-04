from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Question


# отображ последние 5 вопросов разделенные запятой от самого нового к самому старому
# Этот код загружает шаблон polls/index.html и передает ему контекст
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # Контекст - это словарь, содержащий название переменных шаблона и соответствующие им значения
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)


# Страница вопроса – показывает вопрос без результатов но с формой для ответа.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Если объект не найден, вызывается исключение Http404
    return render(request, 'polls/detail.html', {'question': question})


# Страница результата опроса – показывает результаты опроса.
def results(request, question_id):
    response = "Вы смотрите на результаты вопроса %s."
    return HttpResponse(response % question_id)


# Обрабатывает процесс опроса – обрабатывает ответ на вопрос.
def vote(request, question_id):
    return HttpResponse("Вы голосуете за вопрос %s." % question_id)
