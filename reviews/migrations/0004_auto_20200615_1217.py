# Generated by Django 3.0.7 on 2020-06-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200612_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
