# Generated by Django 3.2.4 on 2024-08-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_itemcarrito_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
