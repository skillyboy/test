# Generated by Django 5.1.1 on 2024-09-18 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("afriapp", "0009_alter_subcategory_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
