# Generated by Django 4.2.13 on 2024-05-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='confirmada',
            field=models.BooleanField(default=False),
        ),
    ]
