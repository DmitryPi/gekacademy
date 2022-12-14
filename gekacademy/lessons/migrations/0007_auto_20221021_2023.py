# Generated by Django 3.2.16 on 2022-10-21 17:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_alter_achievement_badge'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='answer',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=55), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='exercise',
            name='condition',
            field=models.TextField(default='', verbose_name='Condition'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='expression',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
