# Generated by Django 5.0.1 on 2024-01-14 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descriptions',
            new_name='description',
        ),
    ]