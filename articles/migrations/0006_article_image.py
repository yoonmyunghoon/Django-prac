# Generated by Django 3.1.6 on 2021-02-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210216_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
