# Generated by Django 4.1.13 on 2024-07-18 13:10

import Articles.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='video',
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=Articles.models.get_default_category, on_delete=django.db.models.deletion.SET_DEFAULT, to='Articles.category'),
        ),
    ]
