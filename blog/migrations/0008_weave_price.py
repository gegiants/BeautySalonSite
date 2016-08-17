# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_pricee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weave_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('weave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Weave')),
            ],
        ),
    ]
