# Generated by Django 4.1.7 on 2023-06-09 14:44


import django.db.models.deletion
from django.db import migrations, models

import furniture.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'nw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north_west'
                    ),
                ),
                (
                    'ne_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north-east'
                    ),
                ),
                (
                    'sw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-west'
                    ),
                ),
                (
                    'se_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-east'
                    ),
                ),
                (
                    'width',
                    models.PositiveIntegerField(
                        help_text='Ширина в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Ширина двери',
                    ),
                ),
                (
                    'open_inside',
                    models.BooleanField(
                        help_text='Открытие в помещении - 1, из помещения - 0',
                        verbose_name='Направление открытия двери внутрь помещения',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Дверь в помещении',
                'verbose_name_plural': 'Двери в помещении',
            },
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=128,
                        unique=True,
                        verbose_name='Наименование мебели',
                    ),
                ),
                (
                    'name_english',
                    models.CharField(
                        max_length=128,
                        unique=True,
                        verbose_name='Наименование мебели на английском языке',
                    ),
                ),
                (
                    'length',
                    models.PositiveIntegerField(
                        help_text='Длина в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина мебели',
                    ),
                ),
                (
                    'width',
                    models.PositiveIntegerField(
                        help_text='Ширина в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Ширина мебели',
                    ),
                ),
                (
                    'length_access',
                    models.PositiveIntegerField(
                        help_text='Длина c зоной подхода в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина мебели c зоной подхода',
                    ),
                ),
                (
                    'width_access',
                    models.PositiveIntegerField(
                        help_text='Ширина c зоной подхода в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Ширина мебели c зоной подхода',
                    ),
                ),
                (
                    'image',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to='furniture/',
                        verbose_name='Изображение мебели',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Мебель',
                'verbose_name_plural': 'Мебель',
            },
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'nw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north_west'
                    ),
                ),
                (
                    'ne_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north-east'
                    ),
                ),
                (
                    'sw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-west'
                    ),
                ),
                (
                    'se_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-east'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Размещение мебели в помещении',
                'verbose_name_plural': 'Размещение мебели в помещении',
            },
        ),
        migrations.CreateModel(
            name='PowerSocket',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'nw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north_west'
                    ),
                ),
                (
                    'ne_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north-east'
                    ),
                ),
                (
                    'sw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-west'
                    ),
                ),
                (
                    'se_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-east'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Розетка в помещении',
                'verbose_name_plural': 'Розетки в помещении',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=128, verbose_name='Название помещения'
                    ),
                ),
                (
                    'first_wall',
                    models.PositiveIntegerField(
                        help_text='Длина стены в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина 1 стены',
                    ),
                ),
                (
                    'second_wall',
                    models.PositiveIntegerField(
                        help_text='Длина стены в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина 2 стены',
                    ),
                ),
                (
                    'third_wall',
                    models.PositiveIntegerField(
                        help_text='Длина стены в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина 3 стены',
                    ),
                ),
                (
                    'fourth_wall',
                    models.PositiveIntegerField(
                        help_text='Длина стены в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина 4 стены',
                    ),
                ),
                (
                    'furniture_placement',
                    models.ManyToManyField(
                        through='furniture.Placement', to='furniture.furniture'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Помещение',
                'verbose_name_plural': 'Помещения',
            },
        ),
        migrations.CreateModel(
            name='Window',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'nw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north_west'
                    ),
                ),
                (
                    'ne_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата north-east'
                    ),
                ),
                (
                    'sw_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-west'
                    ),
                ),
                (
                    'se_coordinate',
                    models.PositiveIntegerField(
                        default=0, verbose_name='Координата south-east'
                    ),
                ),
                (
                    'length',
                    models.PositiveIntegerField(
                        help_text='Длина в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Длина окна',
                    ),
                ),
                (
                    'width',
                    models.PositiveIntegerField(
                        help_text='Ширина в мм',
                        validators=[
                            furniture.models.minimum_len_width_validator
                        ],
                        verbose_name='Ширина окна',
                    ),
                ),
                (
                    'room',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='%(class)ss',
                        to='furniture.room',
                        verbose_name='Комната',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Окно в помещении',
                'verbose_name_plural': 'Окна в помещении',
            },
        ),
    ]
