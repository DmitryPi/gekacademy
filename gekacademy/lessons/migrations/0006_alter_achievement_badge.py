# Generated by Django 3.2.16 on 2022-10-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_achievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='badge',
            field=models.ImageField(blank=True, default='badges/default.png', upload_to='badges/', verbose_name='Badge'),
        ),
    ]
