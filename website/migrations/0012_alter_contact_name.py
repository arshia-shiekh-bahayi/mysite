# Generated by Django 3.2.23 on 2024-03-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
