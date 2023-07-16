from django.db import models
from django.urls import reverse

# Создадим таблицу cats которая будет содержать информацию о кошках
class Cats(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    # для отображения заголовком при выводе "Cats.objects.all()"
    def __str__(self):
        return self.title

    # для формирования нужного маршрута для конкретной записи
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    # Настрйка отображения модели в админ-панели
    class Meta:
        verbose_name = "Famous cats"
        verbose_name_plural = "Famous cats"
        ordering = ['time_create', 'title']


# Модель для таблицы с категориями
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
