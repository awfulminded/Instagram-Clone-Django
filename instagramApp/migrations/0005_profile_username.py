# Generated by Django 4.0.3 on 2022-04-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramApp', '0004_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
