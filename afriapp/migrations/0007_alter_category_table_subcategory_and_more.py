# Generated by Django 4.1 on 2024-09-05 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("afriapp", "0006_alter_product_subcategory_alter_category_table_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="category",
            table="category",
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategories",
                        to="afriapp.category",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="afriapp.subcategory",
            ),
        ),
    ]
