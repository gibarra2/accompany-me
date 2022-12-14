# Generated by Django 4.0.6 on 2022-08-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_alter_place_address_alter_place_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=10, null=True),
        ),
    ]
