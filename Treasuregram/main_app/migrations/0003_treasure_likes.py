# Generated by Django 2.0.2 on 2018-02-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_treasure_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]