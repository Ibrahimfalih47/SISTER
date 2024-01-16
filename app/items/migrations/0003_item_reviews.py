# Generated by Django 5.0.1 on 2024-01-14 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_rename_descriptions_item_description'),
        ('reviews', '0002_remove_review_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='reviews.review'),
        ),
    ]
