# Generated by Django 4.0.3 on 2022-03-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_app_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
