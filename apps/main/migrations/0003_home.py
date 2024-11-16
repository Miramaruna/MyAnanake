# Generated by Django 5.1.3 on 2024-11-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_personal_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(verbose_name='Github домашней страницы')),
                ('twitter', models.URLField(verbose_name='twiiter домашней страницы')),
                ('facebook', models.URLField(verbose_name='facebook домашней страницы')),
                ('google', models.URLField(verbose_name='Google домашней страницы')),
            ],
        ),
    ]