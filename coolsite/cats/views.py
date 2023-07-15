from django.http import HttpResponse
from django.shortcuts import render

# функция представления для главной страницы
def index(request): # request - это ссылка на класс HttpRequest
    # на выходе эта функция формирует экземпляр класса HttpResponse
    return HttpResponse("Страница приложения Cats")

# отображения списка статей по рубрикам
def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")