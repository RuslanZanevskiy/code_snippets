# Generated by Django 4.0.4 on 2022-06-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название языка программирования')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название тега')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название фрагмента кода')),
                ('content', models.TextField(verbose_name='Фрагмент кода(контент)')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_favorite', models.BooleanField(blank=True, default=False, verbose_name='Является ли очень полезным')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='snippets.language', verbose_name='Язык прогроммирования')),
                ('tags', models.ManyToManyField(to='snippets.tag', verbose_name='Теги')),
            ],
        ),
    ]
