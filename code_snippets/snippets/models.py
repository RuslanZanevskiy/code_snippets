from django.db import models


class Language(models.Model):
    name = models.CharField(verbose_name='Название языка программирования', max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name='Название тега', max_length=100)

    def __str__(self):
        return self.name

class Snippet(models.Model):
    name = models.CharField(verbose_name='Название фрагмента кода', max_length=100)
    content = models.TextField(verbose_name='Фрагмент кода(контент)')
    creation_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_favorite = models.BooleanField(default=False, blank=True, verbose_name='Является ли очень полезным')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    language = models.ForeignKey(Language, verbose_name='Язык прогроммирования', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
