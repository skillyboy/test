# Generated by Django 5.1.1 on 2024-09-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("afriapp", "0010_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="options",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
