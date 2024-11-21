# Generated by Django 3.2.23 on 2024-03-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_alter_contact_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Newsletter",
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
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ("created_date",)},
        ),
    ]
