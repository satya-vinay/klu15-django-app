# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 08:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('credits', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(b'Bio-Technology(BT)', b'Bio-Technology(BT)'), (b'Civil Engineering(CE)', b'Civil Engineering(CE)'), (b'Computer Science and Engineering(CSE)', b'Computer Science and Engineering(CSE)'), (b'Electronics and Communication Engineering(ECE)', b'Electronics and Communication Engineering(ECE)'), (b'Electronics and Computer Engineering(ECM)', b'Electronics and Computer Engineering(ECM)'), (b'Electrical and Electronics Engineering(EEE)', b'Electrical and Electronics Engineering(EEE)'), (b'Mechanical Engineering(ME)', b'Mechanical Engineering(ME)'), (b'Petroleum Engineering(PE)', b'Petroleum Engineering(PE)')], default='', max_length=100)),
                ('batch', models.CharField(choices=[(b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Noticeboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=500)),
                ('post', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Category')),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rango.Course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(blank=True, max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ManyToManyField(to='rango.Department'),
        ),
    ]
