# Generated by Django 3.0 on 2020-08-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us_county', '0002_auto_20200818_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uscounty',
            name='full_name',
        ),
        migrations.AddField(
            model_name='uscounty',
            name='fips',
            field=models.CharField(max_length=256, null=True),
        ),
    ]