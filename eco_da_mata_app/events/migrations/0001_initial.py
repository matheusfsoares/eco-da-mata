# Generated by Django 5.0.6 on 2024-05-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('adress', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=100)),
                ('link', models.TextField()),
            ],
        ),
    ]
