from django.db import models
from django.urls import reverse

# Модель для таблицы со статьями о кошках
class Cats(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    # Для формирования нужного маршрута для конкретной записи
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # Настройка отображения модели в админ-панели
    class Meta:
        verbose_name = "Famous cats"
        verbose_name_plural = "Famous cats"
        ordering = ['id']


# Модель для таблицы с категориями
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
