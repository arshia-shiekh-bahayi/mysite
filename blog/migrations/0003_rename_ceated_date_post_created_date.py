# Generated by Django 3.2.23 on 2024-02-22 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240220_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ceated_date',
            new_name='created_date',
        ),
    ]
