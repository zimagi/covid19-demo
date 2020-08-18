# Generated by Django 3.0 on 2020-08-18 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('us_state', '0001_initial'),
        ('us_county', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uscounty',
            name='us_state',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uscounty_relation', to='us_state.USState'),
        ),
        migrations.AlterUniqueTogether(
            name='uscounty',
            unique_together={('us_state', 'name')},
        ),
    ]
