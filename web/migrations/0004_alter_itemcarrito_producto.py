# Generated by Django 3.2.4 on 2024-08-09 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_carrito_itemcarrito_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrito',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.flan'),
        ),
    ]
