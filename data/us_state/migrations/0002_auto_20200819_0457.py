# Generated by Django 3.0 on 2020-08-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us_state', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usstate',
            name='full_name',
        ),
        migrations.AddField(
            model_name='usstate',
            name='fips',
            field=models.CharField(max_length=256, null=True),
        ),
    ]