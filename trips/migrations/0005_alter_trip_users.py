# Generated by Django 4.0.6 on 2022-08-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_dummyuser'),
        ('trips', '0004_alter_place_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='trips', to='profiles.dummyuser'),
        ),
    ]
