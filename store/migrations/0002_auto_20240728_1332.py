# Generated by Django 3.1 on 2024-07-28 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_availabale',
            new_name='is_available',
        ),
    ]
