# Generated by Django 2.2.28 on 2022-06-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athletic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('initials', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
    ]