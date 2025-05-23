# Generated by Django 4.1.13 on 2024-07-18 12:42

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/Category')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, unique=True)),
                ('description', models.TextField()),
                ('preview_description', models.TextField(max_length=300)),
                ('video', models.FileField(blank=True, null=True, upload_to='video/Article')),
                ('image', models.ImageField(upload_to='images/Article')),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
                ('keywords', models.TextField(blank=True, max_length=300, null=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.category')),
            ],
        ),
    ]
