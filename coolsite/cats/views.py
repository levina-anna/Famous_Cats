from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

# Класс для главной страницы "index.html"
class CatsHome(DataMixin, ListView):
    model = Cats
    template_name = 'cats/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cats.objects.filter(is_published=True).select_related('cat')


# Класс для страницы "about.html"
class AboutView(DataMixin, View):
    def get(self, request):
        context = {
            'title': 'About website',
            'menu':  self.get_menu(),
        }
        return render(request, 'cats/about.html', context)

    def get_menu(self):
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        return user_menu


# Класс для страницы "addpage.html"
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'cats/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add page")
        return dict(list(context.items()) + list(c_def.items()))


# Класс для страницы "contact.html"
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'cats/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(selfself, form):
        print(form.cleaned_data)
        return redirect('home')


# Обработчик для страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Класс для отображения поста
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
        return Cats.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category -' + str(c.name),
        cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


# Класс для регистрации
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cats/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign In")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# Класс для авторизации
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cats/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Log In")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


# Функция для выхода пользователя
def logout_user(request):
    logout(request)
    return redirect('login')
