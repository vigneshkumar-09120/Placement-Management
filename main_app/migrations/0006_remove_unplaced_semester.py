# Generated by Django 4.1.4 on 2023-01-19 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_graduated_date_of_join_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unplaced',
            name='semester',
        ),
    ]
