from django.db import models

sem_choices = (
    ("8","8"),
    ("7","7"),
)

higher_choices =(
    ("Yes","Yes"),
    ("No","No"),
)
campus_choices=(
    (" On Campus"," On Campus"),
    (" Off Campus"," Off Campus"),
)
Type_choices =(
    (" Open Dream"," Open Dream"),
    (" Dream"," Dream"),
)
drive=(
    ("Interview","Interview"),
    ("Test","Test"),
)
sem = (
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
)



# Create your models here.
class Internship(models.Model):
    Usn = models.CharField(max_length=15)
    Full_name=models.CharField(max_length=50)
    semester=models.CharField(max_length=15,choices=sem)
    rvce_email=models.CharField(max_length=50)
    personal_email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    Interested_In_higherStudies=models.CharField(max_length=5,choices=higher_choices)
    Company=models.CharField(max_length=25)
    Date_of_offer=models.DateField(max_length=25)
    Start_date=models.DateField(max_length=25)
    End_date=models.DateField(max_length=25)
    Role=models.CharField(max_length=20)
    Type=models.CharField(max_length=20,choices=campus_choices)
    Stipend=models.IntegerField(default=0)
    Internal_Guide_name=models.CharField(max_length=50)
    External_Guide_name=models.CharField(max_length=50)

class Placements(models.Model):
    Usn = models.CharField(max_length=15)
    Full_name=models.CharField(max_length=50)
    semester=models.CharField(max_length=15,choices=sem_choices)
    rvce_email=models.CharField(max_length=50)
    personal_email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    Interested_In_higherStudies=models.CharField(max_length=5,choices=higher_choices)
    Category=models.CharField(max_length=20,choices=Type_choices)
    Company=models.CharField(max_length=25)
    Company_addr=models.CharField(max_length=300)
    Intern=models.CharField(max_length=5,choices=higher_choices)
    Duration_of_Internship=models.IntegerField(default=0)
    Ppo=models.CharField(max_length=15,choices=higher_choices)
    Fte=models.CharField(max_length=15,choices=higher_choices)
    Date_of_offer=models.DateField(max_length=25)
    Role=models.CharField(max_length=20)
    Ctc=models.FloatField(default=0)
  
class Graduated(models.Model):
    Usn = models.CharField(max_length=15,blank=True,default=None)
    Full_name=models.CharField(max_length=50)
    personal_email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    Date_of_Grad=models.DateField(max_length=20)
    Gre_score=models.FloatField(default=0,blank=True)
    Gmat_score=models.FloatField(default=0,blank=True)
    Toefl_score=models.FloatField(default=0,blank=True)
    Ielts_score=models.FloatField(default=0,blank=True)
    Gate_score=models.FloatField(default=0,blank=True)
    Other_score=models.CharField(max_length=30,blank=True,default=None)
    University=models.CharField(max_length=300,blank=True,default=None)
    Specialization=models.CharField(max_length=50,blank=True,default=None)
    Date_of_Join=models.DateField(max_length=20,blank=True,null=True)
    Date_of_UniGrad=models.DateField(max_length=20,blank=True,null=True)
    Current_profile_details=models.CharField(max_length=400,blank=True,default=None)
    Role=models.CharField(max_length=50,blank=True,default=None)
    Salary=models.FloatField(default=0,blank=True)

class Unplaced(models.Model):
    Usn = models.CharField(max_length=15)
    Full_name=models.CharField(max_length=50)
    
    rvce_email=models.CharField(max_length=50)
    personal_email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    Interested_In_higherStudies=models.CharField(max_length=5,choices=higher_choices)
    Eligible=models.CharField(max_length=5,choices=higher_choices,default='No')
    Ten_score=models.FloatField(default=0)
    Twelth_score=models.FloatField(default=0)
    first_cgpa=models.FloatField(default=0)
    sec_cgpa=models.FloatField(default=0)
    third_cgpa=models.FloatField(default=0)
    four_cgpa=models.FloatField(default=0)
    five_cgpa=models.FloatField(default=0)
    six_cgpa=models.FloatField(default=0)
    seven_cgpa=models.FloatField(default=0)
    eight_cgpa=models.FloatField(default=0)
    Remarks=models.CharField(max_length=400)

class Drive(models.Model):
    Usn = models.CharField(max_length=15)
    Full_name=models.CharField(max_length=50)
    semester=models.CharField(max_length=15,choices=sem)
    rvce_email=models.CharField(max_length=50)
    personal_email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    Interested_In_higherStudies=models.CharField(max_length=5,choices=higher_choices)
    Company=models.CharField(max_length=20)
    Date_of_drive=models.DateField(max_length=20)
    Type=models.CharField(max_length=20,choices=drive)

class Document(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'documents'

class Faculty(models.Model):
    Name=models.CharField(max_length=25)
    email=models.CharField(max_length=100)
    semester=models.CharField(max_length=25,choices=sem)        
    

    
    













