from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


# функция представления для главной страницы
def index(request):
    # Выберем все записи из таблицы и сохраним их в переменную
    posts = Cats.objects.all()
    return render(request, 'cats/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

# функция представления для страницы "О сайте"
def about(request):
    return render(request, 'cats/about.html', {'menu': menu, 'title': 'О сайте'})


# отображения списка статей по рубрикам
def categories(request, categoriesid): # http://127.0.0.1:8000/categories/1/?name=Moosya&type=siberian
    if(request.GET):
        print(request.GET) # {'name': ['Moosya'], 'type': ['siberian']}

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{categoriesid}</p>")

def archive(request, year):
    if int(year) > 2020: # http://127.0.0.1:8000/archive/2022
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# Обработчик для страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')