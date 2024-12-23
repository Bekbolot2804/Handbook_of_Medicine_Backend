# Generated by Django 5.1.4 on 2024-12-22 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=520, verbose_name='Описание')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фото логотипа компании')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.authuser', verbose_name='Создатель акции')),
            ],
        ),
        migrations.CreateModel(
            name='Lesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название поражения')),
                ('status', models.CharField(max_length=20, verbose_name='Статус')),
                ('date_start', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
                ('date_applied', models.DateTimeField(blank=True, null=True, verbose_name='Дата подачи заявки')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='creator_lesions', to='main.authuser', verbose_name='Создатель')),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderator_lesions', to='main.authuser', verbose_name='Модератор')),
            ],
        ),
        migrations.CreateModel(
            name='HelpLesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время')),
                ('comment', models.CharField(max_length=249, verbose_name='Комментарий')),
                ('help', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_lesions', to='main.help', verbose_name='Помощь')),
                ('lesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesion_helps', to='main.lesion', verbose_name='Поражение')),
            ],
        ),
    ]
