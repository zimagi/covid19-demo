# Generated by Django 3.0 on 2020-08-18 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('us_state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USStateMeasures',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('date', models.DateField(null=True)),
                ('positive', models.IntegerField(null=True)),
                ('negative', models.IntegerField(null=True)),
                ('pending', models.IntegerField(null=True)),
                ('recovered', models.IntegerField(null=True)),
                ('deaths', models.IntegerField(null=True)),
                ('hospitalized', models.IntegerField(null=True)),
                ('hospitalized_currently', models.IntegerField(null=True)),
                ('hospitalized_cumulative', models.IntegerField(null=True)),
                ('icu_currently', models.IntegerField(null=True)),
                ('icu_cumulative', models.IntegerField(null=True)),
                ('ventilator_currently', models.IntegerField(null=True)),
                ('ventilator_cumulative', models.IntegerField(null=True)),
                ('total_test_results', models.IntegerField(null=True)),
                ('total_tests_viral', models.IntegerField(null=True)),
                ('positive_tests_viral', models.IntegerField(null=True)),
                ('negative_tests_viral', models.IntegerField(null=True)),
                ('positive_cases_viral', models.IntegerField(null=True)),
                ('death_confirmed', models.IntegerField(null=True)),
                ('death_probable', models.IntegerField(null=True)),
                ('us_state', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usstatemeasures_relation', to='us_state.USState')),
            ],
            options={
                'verbose_name': 'us state measures',
                'verbose_name_plural': 'us state measuress',
                'db_table': 'covid19_us_state_measures',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('us_state', 'name')},
            },
        ),
    ]
