# Generated by Django 4.2.11 on 2024-04-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_cat_feeding_finch'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='is_hungry',
            field=models.BooleanField(default=True),
        ),
    ]
