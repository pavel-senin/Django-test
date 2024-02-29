from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def home(request):
    html = "<h1>Добро пожаловать на мой первый Django-сайт!</h1>"

    logger.info("Посещена главная страница")

    return render(request, 'myapp/home.html', {'html': html})

def about(request):
    html = "<h1>Обо мне</h1><p>Это моя первая Django-страница. Я изучаю Django и создаю свой первый проект.</p>"

    logger.info("Посещена страница 'О себе'")

    return render(request, 'myapp/about.html', {'html': html})
