# Generated by Django 3.2.8 on 2021-10-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.SlugField(max_length=30),
        ),
    ]
