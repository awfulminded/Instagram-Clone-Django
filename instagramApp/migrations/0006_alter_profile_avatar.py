# Generated by Django 4.0.3 on 2022-04-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramApp', '0005_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
