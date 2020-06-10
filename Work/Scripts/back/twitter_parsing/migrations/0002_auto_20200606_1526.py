# Generated by Django 3.0.7 on 2020-06-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_parsing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateField(blank=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='negative',
            field=models.BooleanField(blank=True, verbose_name='сентимент'),
        ),
    ]