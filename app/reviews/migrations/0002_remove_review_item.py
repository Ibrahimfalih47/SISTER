# Generated by Django 5.0.1 on 2024-01-14 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='item',
        ),
    ]
