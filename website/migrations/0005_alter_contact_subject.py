# Generated by Django 3.2.23 on 2024-03-13 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_auto_20240312_1752"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="subject",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
