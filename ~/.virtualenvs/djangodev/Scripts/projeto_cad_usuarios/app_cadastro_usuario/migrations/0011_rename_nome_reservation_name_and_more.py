# Generated by Django 5.0.3 on 2024-06-29 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuario', '0010_alter_reservation_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='timeslots',
            new_name='timeslot',
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('data', 'timeslot')},
        ),
    ]
