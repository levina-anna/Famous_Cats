from django.http import HttpResponse
from django.shortcuts import render

# функция представления для главной страницы
def index(request): # request - это ссылка на класс HttpRequest
    # на выходе эта функция формирует экземпляр класса HttpResponse
    return HttpResponse("Страница приложения Cats")

# отображения списка статей по рубрикам
def categories(request, categoriesid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{categoriesid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")