from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "About website", 'url_name': 'about'},
        {'title': "Add page", 'url_name': 'add_page'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "Log In", 'url_name': 'login'},

]


# функция представления для главной страницы
def index(request):
    # Выберем все записи из таблицы и сохраним их в переменную
    posts = Cats.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }

    return render(request, 'cats/index.html', context=context)


# функция представления для страницы "О сайте"
def about(request):
    return render(request, 'cats/about.html', {'menu': menu, 'title': 'О сайте'})


# функция представления для страницы "Добавление статьи"
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Cats.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Error adding post")
    else:
        form = AddPostForm()
    return render(request, 'cats/addpage.html', {'form': form, 'menu': menu, 'title': "Add post"})


# функция представления для страницы "Обратная связь"
def contact(request):
    return HttpResponse("Обратная связь")


# функция представления для страницы "Авторизация"
def login(request):
    return HttpResponse("Авторизация")


# Обработчик для страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Обработчик страницы "Read post"
def show_post(request, post_slug):
    post = get_object_or_404(Cats, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'cats/post.html', context=context)


# Обработчик для категорий
def show_category(request, cat_id):
    posts = Cats.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Display by category',
        'cat_selected': cat_id,
    }

    return render(request, 'cats/index.html', context=context)