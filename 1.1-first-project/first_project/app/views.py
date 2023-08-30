from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import locale
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    if 'ru' in request.META.get('HTTP_ACCEPT_LANGUAGE'):
        locale.setlocale(
            category=locale.LC_ALL,
            locale="Russian"
        )
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%d-%b-%Y %H:%M:%S.%f")
    msg = f'Текущее время: {current_time_str}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    rez = sorted(os.listdir(path='.'))
    return HttpResponse("<br>".join([item for item in rez]))
    # raise NotImplemented
