# Generated by Django 5.0.3 on 2024-06-12 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuario', '0007_alter_reservation_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='data',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
    ]
