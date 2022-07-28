# Generated by Django 4.0.6 on 2022-07-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('is_logged_in', models.BooleanField(default=False)),
            ],
        ),
    ]
