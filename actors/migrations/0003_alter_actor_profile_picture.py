# Generated by Django 4.0.5 on 2022-06-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_actor_age_alter_actor_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='profile_picture',
            field=models.ImageField(upload_to='actors/'),
        ),
    ]
