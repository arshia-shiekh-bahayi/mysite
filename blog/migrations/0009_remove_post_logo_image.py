# Generated by Django 3.2.23 on 2024-03-09 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_logo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='logo_image',
        ),
    ]
