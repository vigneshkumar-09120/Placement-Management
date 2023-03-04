from django.forms import ValidationError
import pandas as pd

from .models import Placements


def handle_csv(file):
    data = pd.read_csv(file)
    try:
        for _, row in data.iterrows():
            Usn = row['USN']
            Full_name = row['FULL NAME']
            semester = row['SEM']
            rvce_email = row['RVCE EMAIL']
            personal_email = row['PERSONAL EMAIL']
            phone = row['PHONE']
            Interested_In_higherStudies = row['INTERESTED IN HIGHER STUDIES']
            Category = row['CATEGORY']
            Company = row['COMPANY']
            Company_addr = row['COMPANY ADDR']
            Intern = row['INTERN']
            Duration_of_Internship = row['DURATION OF INTERNSHIP']
            Ppo = row['PPO']
            Fte= row['FTE']
            Date_of_offer = row['DATE OF OFFER']
            Role = row['ROLE']
            Ctc = row['CTC']
            
        
       
            placed = Placements.objects.create(
            Usn=Usn,Full_name=Full_name,semester=semester,rvce_email=rvce_email,personal_email=personal_email,phone=phone,Interested_In_higherStudies= Interested_In_higherStudies,
            Category=Category,Company=Company,Company_addr=Company_addr,Intern=Intern,Duration_of_Internship=Duration_of_Internship,Ppo=Ppo,Fte=Fte,Date_of_offer=Date_of_offer,Role=Role,Ctc=Ctc)
            placed.save()
        return True
    except Exception as e:
        print(e)
        return False    