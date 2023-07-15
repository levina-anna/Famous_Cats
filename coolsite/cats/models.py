from django.db import models

# Создадим таблицу cats которая будет содержать информацию о кошках

class Cats(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # для отображения заголовком при выводе "Cats.objects.all()"
    def __str__(self):
        return self.title
