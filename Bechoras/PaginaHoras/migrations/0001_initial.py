# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('idActividad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=64)),
                ('date', models.DateTimeField()),
                ('horas', models.IntegerField()),
                ('carne', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AsigActividad',
            fields=[
                ('idAsigActividad', models.IntegerField(primary_key=True, serialize=False)),
                ('idActividad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet', models.IntegerField()),
                ('nombre', models.CharField(max_length=64)),
                ('correo', models.EmailField(max_length=64)),
                ('contrasena', models.CharField(max_length=64)),
                ('horasPendientes', models.IntegerField()),
                ('horasRealizadas', models.IntegerField()),
                ('admin', models.BooleanField()),
            ],
        ),
    ]