# Generated by Django 5.0.7 on 2024-07-30 19:52

import BackEnd.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0004_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='release_date',
            field=models.IntegerField(default=1900, validators=[BackEnd.models.validate_year]),
            preserve_default=False,
        ),
    ]
