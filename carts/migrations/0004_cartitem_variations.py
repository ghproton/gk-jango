# Generated by Django 3.1 on 2024-08-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_variation'),
        ('carts', '0003_auto_20240801_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
