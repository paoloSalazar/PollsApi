# Generated by Django 3.0.5 on 2020-04-08 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='choices',
        ),
        migrations.AlterModelTable(
            name='poll',
            table='polls',
        ),
        migrations.AlterModelTable(
            name='vote',
            table='votes',
        ),
    ]
