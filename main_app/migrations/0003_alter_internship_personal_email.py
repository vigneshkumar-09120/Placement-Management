# Generated by Django 4.1.4 on 2023-01-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_internship_personal_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='personal_email',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
