# Generated by Django 3.0.6 on 2020-05-23 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('player', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('team', models.CharField(blank=True, max_length=3, null=True)),
                ('position', models.CharField(blank=True, max_length=2, null=True)),
                ('gamesplayed', models.IntegerField(blank=True, null=True)),
                ('goals', models.IntegerField(blank=True, null=True)),
                ('assists', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('plusminus', models.IntegerField(blank=True, null=True)),
                ('pim', models.IntegerField(blank=True, null=True)),
                ('pointshares', models.FloatField(blank=True, null=True)),
                ('evgoals', models.IntegerField(blank=True, null=True)),
                ('ppgoals', models.IntegerField(blank=True, null=True)),
                ('shgoals', models.IntegerField(blank=True, null=True)),
                ('gwgoals', models.IntegerField(blank=True, null=True)),
                ('evassists', models.IntegerField(blank=True, null=True)),
                ('ppassists', models.IntegerField(blank=True, null=True)),
                ('shassists', models.IntegerField(blank=True, null=True)),
                ('shots', models.IntegerField(blank=True, null=True)),
                ('shootingpercentage', models.FloatField(blank=True, null=True)),
                ('toi', models.IntegerField(blank=True, null=True)),
                ('atoi', models.CharField(blank=True, max_length=5, null=True)),
                ('blocks', models.IntegerField(blank=True, null=True)),
                ('hits', models.IntegerField(blank=True, null=True)),
                ('faceoffwins', models.IntegerField(blank=True, null=True)),
                ('faceofflosses', models.IntegerField(blank=True, null=True)),
                ('faceoffwinpercentage', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stats',
                'managed': False,
            },
        ),
    ]
