from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

# Класс для главной страницы index.html
class CatsHome(DataMixin, ListView):
    model = Cats
    template_name = 'cats/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cats.objects.filter(is_published=True)


# функция представления для страницы "О сайте"
def about(request):
    return render(request, 'cats/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'cats/addpage.html'
    # адрес маршрута куда мы должны перенаправиться когда доб статью
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add category")
        return dict(list(context.items()) + list(c_def.items()))


# функция представления для страницы "Обратная связь"
def contact(request):
    return HttpResponse("Обратная связь")


# функция представления для страницы "Авторизация"
def login(request):
    return HttpResponse("Авторизация")


# Обработчик для страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DetailView):
    model = Cats
    template_name = 'cats/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# Класс для категорий
class CatsCategory(DataMixin, ListView):
    model = Cats
    template_name = 'cats/index.html'
    context_object_name = 'posts'
    allow_empty = False

    # выбрать только те записи которым соответствует категория по указанному слагу
    def get_queryset(self):
        return Cats.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category -' + str(context['posts'][0].cat),
        cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
