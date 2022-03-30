# Generated by Django 4.0.3 on 2022-03-30 16:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Unique Verification UUID'),
        ),
    ]
