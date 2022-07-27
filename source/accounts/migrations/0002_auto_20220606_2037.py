# Generated by Django 2.2.28 on 2022-06-06 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_federated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_graduated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
