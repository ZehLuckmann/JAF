# Generated by Django 2.2.28 on 2022-06-07 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletic', '0001_initial'),
        ('accounts', '0003_auto_20220606_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='athletic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='athletic.Athletic'),
        ),
    ]