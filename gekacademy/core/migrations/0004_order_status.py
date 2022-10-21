# Generated by Django 3.2.16 on 2022-10-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221016_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('PENDING', 'Pending'), ('SUCCESS', 'Success')], default='PENDING', max_length=55),
        ),
    ]