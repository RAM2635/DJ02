from django.db import models

class News(models.Model):
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")
    title = models.CharField(max_length=50, verbose_name="Название новости")
    description = models.CharField(verbose_name="Краткое описание новости", max_length=200)
    content = models.TextField(verbose_name="Новость")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title
