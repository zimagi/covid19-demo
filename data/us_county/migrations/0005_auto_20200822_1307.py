# Generated by Django 3.0 on 2020-08-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us_county', '0004_auto_20200822_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uscounty',
            name='fips',
            field=models.IntegerField(null=True),
        ),
    ]