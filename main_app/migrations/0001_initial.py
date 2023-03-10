# Generated by Django 4.1.4 on 2023-01-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usn', models.CharField(max_length=15)),
                ('Full_name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('4', '4'), ('5', '5')], max_length=15)),
                ('rvce_email', models.CharField(max_length=50)),
                ('personal_email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('Interested_In_higherStudies', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('Company', models.CharField(max_length=20)),
                ('Date_of_drive', models.DateField(max_length=20)),
                ('Type', models.CharField(choices=[('Interview', 'Interview'), ('Test', 'Test')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Graduated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usn', models.CharField(max_length=15, null=True)),
                ('Full_name', models.CharField(max_length=50)),
                ('personal_email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('Date_of_Grad', models.DateField(max_length=20)),
                ('Gre_score', models.FloatField(default=0, null=True)),
                ('Gmat_score', models.FloatField(default=0, null=True)),
                ('Toefl_score', models.FloatField(default=0, null=True)),
                ('Ielts_score', models.FloatField(default=0, null=True)),
                ('Gate_score', models.FloatField(default=0, null=True)),
                ('Other_score', models.CharField(max_length=30, null=True)),
                ('University', models.CharField(max_length=300, null=True)),
                ('Specialization', models.CharField(max_length=50, null=True)),
                ('Date_of_Join', models.DateField(max_length=20, null=True)),
                ('Date_of_UniGrad', models.DateField(max_length=20, null=True)),
                ('Current_profile_details', models.CharField(max_length=400, null=True)),
                ('Role', models.CharField(max_length=50, null=True)),
                ('Salary', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usn', models.CharField(max_length=15)),
                ('Full_name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('4', '4'), ('5', '5')], max_length=15)),
                ('rvce_email', models.CharField(max_length=50)),
                ('personal_email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('Interested_In_higherStudies', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('Company', models.CharField(max_length=25)),
                ('Date_of_offer', models.DateField(max_length=25)),
                ('Start_date', models.DateField(max_length=25)),
                ('End_date', models.DateField(max_length=25)),
                ('Role', models.CharField(max_length=20)),
                ('Type', models.CharField(choices=[('On Campus', 'On Campus'), ('Off Campus', 'Off Campus')], max_length=15)),
                ('Stipend', models.IntegerField(default=0)),
                ('Internal_Guide_name', models.CharField(max_length=50)),
                ('External_Guide_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usn', models.CharField(max_length=15)),
                ('Full_name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('4', '4'), ('5', '5')], max_length=15)),
                ('rvce_email', models.CharField(max_length=50)),
                ('personal_email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('Interested_In_higherStudies', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('Category', models.CharField(choices=[('Open Dream', 'Open Dream'), ('Dream', 'Dream')], max_length=10)),
                ('Company', models.CharField(max_length=25)),
                ('Company_addr', models.CharField(max_length=300)),
                ('Intern', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('Duration_of_Internship', models.IntegerField(default=0)),
                ('Ppo', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('Fte', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('Date_of_offer', models.DateField(max_length=25)),
                ('Role', models.CharField(max_length=20)),
                ('Ctc', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Unplaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usn', models.CharField(max_length=15)),
                ('Full_name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('4', '4'), ('5', '5')], max_length=15)),
                ('rvce_email', models.CharField(max_length=50)),
                ('personal_email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('Interested_In_higherStudies', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('Ten_score', models.FloatField(default=0)),
                ('Twelth_score', models.FloatField(default=0)),
                ('first_cgpa', models.FloatField(default=0)),
                ('sec_cgpa', models.FloatField(default=0)),
                ('third_cgpa', models.FloatField(default=0)),
                ('four_cgpa', models.FloatField(default=0)),
                ('five_cgpa', models.FloatField(default=0)),
                ('six_cgpa', models.FloatField(default=0)),
                ('seven_cgpa', models.FloatField(default=0)),
                ('eight_cgpa', models.FloatField(default=0)),
                ('Remarks', models.CharField(max_length=400)),
            ],
        ),
    ]
