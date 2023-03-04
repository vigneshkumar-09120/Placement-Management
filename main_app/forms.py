from django import forms
from django.core.exceptions import ValidationError
from .models import Internship,Placements,Graduated,Unplaced,Drive,Document
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Internshipform(forms.ModelForm):
    class Meta:
        model=Internship
        fields= '__all__'
        widgets = {
            'Usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'Full_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Full Name"}),
            'semester': forms.Select(attrs={"class": "form-control", "placeholder": "Select the semester"}),
            'rvce_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'Interested_In_higherStudies': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Company': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Company Name"}),
            
            'Date_of_offer':AdminDateWidget(attrs={'type': 'date',"class": "form-control", "placeholder": "Select The Date Of Offer"}),
            'Start_date': forms.DateInput(attrs={'type': 'date',"class": "form-control", "placeholder": "Select Start date of Internship"}),
            'End_date': forms.DateInput(attrs={'type': 'date',"class": "form-control", "placeholder": "Select End date of the Internship"}),
            'Role': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Role"}),
            'Type': forms.Select(attrs={"class": "form-control", "placeholder": "Select On or Off Campus"}),
            'Stipend': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter the Stipend"}),
            'Internal_Guide_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Internal Guide Name"}),
            'External_Guide_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the External Guide Name"}), 
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        )
    )

class Placementsform(forms.ModelForm):
    class Meta:
        model=Placements
        fields= '__all__'
        widgets = {
            'Usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'Full_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Full Name"}),
            'semester': forms.Select(attrs={"class": "form-control", "placeholder": "Select the semester"}),
            'rvce_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'Interested_In_higherStudies': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Category': forms.Select(attrs={"class": "form-control", "placeholder": "Select the Category"}),
            'Company': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Company Name"}),
            'Company_addr': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Company Address"}),
            'Intern':forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            
            'Duration_of_Internship': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter the Duration of Internship in months"}),
            'Ppo': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Fte': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Date_of_offer':AdminDateWidget(attrs={'type': 'date',"class": "form-control", "placeholder": "Select The Date Of Offer"}),
            
            'Role': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Role"}),
            'Ctc':forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter the CTC "}),
           
        }


class Graduatedform(forms.ModelForm):
    class Meta:
        model=Graduated
        fields= '__all__'
        widgets = {
            'Usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'Full_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Full Name"}),
           
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'Date_of_Grad':AdminDateWidget(attrs={'type': 'date',"class": "form-control", "placeholder": "Select The Date Of Graduation from RVCE"}),
            'Gre_score':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the GRE Score "}),
            'Gmat_score':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the GMAT Score "}),
            'Toefl_score':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the TOEFL Score "}),
            'Ielts_score':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the IELTS Score "}),
            'Gate_score':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the GATE Score "}),
            'Other_score':forms.TextInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the any other Exam Score in the format {exam-score} "}),
            'University':forms.Textarea(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the University Details"}),
            'Specialization': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Specialization"}),
            'Date_of_Join':AdminDateWidget(attrs={'type': 'date',"class": "form-control", "placeholder": "Select The Date Of Join of the University"}),
            'Date_of_UniGrad':AdminDateWidget(attrs={'type': 'date',"class": "form-control", "placeholder": "Select The Date Of Gradution from the University"}),
            'Current_profile_details':forms.Textarea(attrs={"class": "form-control", "placeholder": "Describe the current profile Job/Enterpreneur"}),
            'Role': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Role"}),
            'Salary':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the Salary per month in Lakhs "}),
        }

class Unplacedform(forms.ModelForm):
    class Meta:
        model=Unplaced
        fields= '__all__'
        widgets = {
            'Usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'Full_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Full Name"}),
            
            'rvce_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'Interested_In_higherStudies': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Eligible': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Ten_score':forms.NumberInput(attrs={"class": "form-control", 'step': "0.01","placeholder": "Enter the Tenth Score "}),
            'Twelth_score':forms.NumberInput(attrs={"class": "form-control", 'step': "0.01","placeholder": "Enter the Twelth Score "}),
            'first_cgpa':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the First sem CGPA "}),
            'sec_cgpa':forms.NumberInput(attrs={"class": "form-control", 'step': "0.01","placeholder": "Enter the Second sem CGPA "}),
            'third_cgpa':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the Third sem CGPA "}),
            'four_cgpa':forms.NumberInput(attrs={"class": "form-control", 'step': "0.01","placeholder": "Enter the Fourth sem CGPA "}),
            'five_cgpa':forms.NumberInput(attrs={"class": "form-control", 'step': "0.01","placeholder": "Enter the Fifth sem CGPA "}),
            'six_cgpa':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the Sixth sem CGPA "}),
            'seven_cgpa':forms.NumberInput(attrs={"class": "form-control",'step': "0.01", "placeholder": "Enter the seventh sem CGPA "}),
            'eight_cgpa':forms.NumberInput(attrs={"class": "form-control", 'step': "0.01","placeholder": "Enter the Eighth sem CGPA "}),
            'Remarks':forms.Textarea(attrs={"class": "form-control", "placeholder": "Describe the about  current Status/ any Remarks"}),
        }        
                

class Driveform(forms.ModelForm):
    class Meta:
        model=Drive
        fields= '__all__'
        widgets = {
            'Usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            'Full_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Full Name"}),
            'semester': forms.Select(attrs={"class": "form-control", "placeholder": "Select the semester"}),
            'rvce_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'personal_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'Interested_In_higherStudies': forms.Select(attrs={"class": "form-control", "placeholder": "Select Yes/No"}),
            'Type': forms.Select(attrs={"class": "form-control", "placeholder": "Choose Interview /Test"}),
            'Company': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Company Name"}),
            'Date_of_drive':AdminDateWidget(attrs={'type': 'date',"class": "form-control", "placeholder": "Select The Date Of Offer"}),
        }

class UploadForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith('.csv'):
            raise ValidationError(
                "Only csv file format supported!", code='invalid')
        return file

    class Meta:
        model = Document
        fields = (
            "name",
            "file",
        )
        widgets = {'file': forms.FileInput(attrs={"class": "form-control"})}        