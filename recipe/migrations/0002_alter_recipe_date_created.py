# Generated by Django 4.2.1 on 2023-05-31 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
    ]