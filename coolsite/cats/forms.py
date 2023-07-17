# Тут находятся все формы

from django import forms
from .models import *


# Класс описывающий форму добавления статьи
# выставляем только те атрибуты которые должен вводить пользователь
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Not selected")