# Generated by Django 5.0 on 2023-12-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_profile_app', '0004_remove_user_verification_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
