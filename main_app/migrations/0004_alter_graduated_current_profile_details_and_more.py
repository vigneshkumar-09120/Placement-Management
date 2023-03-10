# Generated by Django 4.1.4 on 2023-01-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_internship_personal_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduated',
            name='Current_profile_details',
            field=models.CharField(blank=True, default=None, max_length=400),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Date_of_Join',
            field=models.DateField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Date_of_UniGrad',
            field=models.DateField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Gate_score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Gmat_score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Gre_score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Ielts_score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Other_score',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Role',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Specialization',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Toefl_score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='University',
            field=models.CharField(blank=True, default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='Usn',
            field=models.CharField(blank=True, default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='internship',
            name='personal_email',
            field=models.CharField(max_length=50),
        ),
    ]
