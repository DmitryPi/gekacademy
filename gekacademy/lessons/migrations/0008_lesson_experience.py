# Generated by Django 3.2.16 on 2022-10-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20221021_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='experience',
            field=models.IntegerField(default=10, verbose_name='Experience'),
        ),
    ]
