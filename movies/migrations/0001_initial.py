# Generated by Django 4.0.5 on 2022-06-09 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0003_alter_actor_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('production_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(default='img.png', upload_to='movies/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('actors', models.ManyToManyField(to='actors.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director', verbose_name='Director')),
            ],
        ),
    ]
