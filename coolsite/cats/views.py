from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "About website", 'url_name': 'about'},
        {'title': "Add page", 'url_name': 'add_page'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "Log In", 'url_name': 'login'},

]

# Класс для главной страницы index.html
class CatsHome(ListView):
    # выбираем все записи из таблицы и отображаем в виде списка
    model = Cats
    # указываем шаблон
    template_name = 'cats/index.html'
    # указываем список для отображения статей (исп в шаблоне)
    context_object_name = 'posts'

    # функция для формирования контекста
    def get_context_data(self, *, object_list=None, **kwargs):
        # взять существующий контекст
        context = super().get_context_data(**kwargs)
        # далее прописываем или меняем атрибуты
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        # возвращаем измененный контекст
        return context

    # Вернуть (читать) только те записи которые опубликованы
    def get_queryset(self):
        return Cats.objects.filter(is_published=True)



# функция представления для главной страницы
# def index(request):
#     # Выберем все записи из таблицы и сохраним их в переменную
#     posts = Cats.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'cats/index.html', context=context)


# функция представления для страницы "О сайте"
def about(request):
    return render(request, 'cats/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'cats/addpage.html'
    # адрес маршрута куда мы должны перенаправиться когда доб статью
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context

# функция представления для страницы "Добавление статьи"
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'cats/addpage.html', {'form': form, 'menu': menu, 'title': "Add post"})


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
# def show_post(request, post_slug):
#     post = get_object_or_404(Cats, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'cats/post.html', context=context)


class ShowPost(DetailView):
    model = Cats
    template_name = 'cats/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context



# Класс для категорий
class CatsCategory(ListView):
    model = Cats
    template_name = 'cats/index.html'
    context_object_name = 'posts'
    allow_empty = False

    # выбрать только те записи которым соответствует категория по указанному слагу
    def get_queryset(self):
        return Cats.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context



# Обработчик для категорий
# def show_category(request, cat_id):
#     posts = Cats.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Display by category',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'cats/index.html', context=context)