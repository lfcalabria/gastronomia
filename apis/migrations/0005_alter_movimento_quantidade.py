# Generated by Django 4.2.13 on 2024-06-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_rename_preco_nitario_itemnotafiscal_preco_unitario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimento',
            name='quantidade',
            field=models.DecimalField(db_comment='Quantidade movimentada', decimal_places=5, max_digits=9),
        ),
    ]
