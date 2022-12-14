# Generated by Django 2.2.28 on 2022-06-07 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20220607_0044'),
        ('tournament', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentModality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='team.Modality')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tournament.Tournament')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='modalities',
            field=models.ManyToManyField(through='tournament.TournamentModality', to='team.Modality'),
        ),
    ]
