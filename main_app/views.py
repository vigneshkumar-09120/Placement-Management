from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import Internshipform , UserLoginForm ,Placementsform,Unplacedform ,Driveform ,Graduatedform,UploadForm
from .models import Internship, Placements,Drive,Unplaced,Graduated,Faculty
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q ,Max ,Min,Avg
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.edit import CreateView, FormView, DeleteView
from .file_handlers import handle_csv
from django.forms import ValidationError
from django.db import models
from email.message import EmailMessage
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage

from django.core import mail

from django.conf import settings
from datetime import datetime, timedelta

# Create your views here.

def Home(request):
    
    return render(request,"home.html")

@login_required 
def Internship_list(request):
    if'q'in request.GET:
        q=request.GET['q']
        #data=Internship.objects.filter(Full_name__icontains=q)
        multiple_q=Q(Q(Full_name__icontains=q)|Q(Usn__icontains=q)|Q(semester__icontains=q)|Q(Type__icontains=q)|Q(Role__icontains=q)|Q(Company__icontains=q))
        data=Internship.objects.filter(multiple_q).order_by('-Usn')
    else:
        data=Internship.objects.all().order_by('-Usn')    
    context={'InternList':data}
    return render(request,"Internship_list.html",context)
    
@login_required
def Internship_form(request,id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id==0:
                form = Internshipform()
            else:
                Intern=Internship.objects.get(pk=id)
                form=Internshipform(instance=Intern)    
            return render(request, "Internship_form.html",{'form':form})
        else:
            if id==0:
                form = Internshipform(request.POST)
            else:
                Intern=Internship.objects.get(pk=id)
                form=Internshipform(request.POST,instance=Intern)   
            if form.is_valid():
                form.save()
            return redirect('/Student_SPC/list')
    else:
        return HttpResponseRedirect('/login/')


def Internship_delete(request,id):
    Intern=Internship.objects.get(pk=id)
    Intern.delete()
    return redirect('/Student_SPC/list')    

def user_login(request):
    if request.method=="POST":
        form=UserLoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect('/Student_SPC/Shome')
                
    else:
        form=UserLoginForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def Placements_form(request,id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id==0:
                form = Placementsform()
            else:
                Place=Placements.objects.get(pk=id)
                form=Placementsform(instance=Place)    
            return render(request, "Placements_form.html",{'form':form})
        else:
            if id==0:
                form = Placementsform(request.POST)
            else:
                Place=Placements.objects.get(pk=id)
                form=Placementsform(request.POST,instance=Place)   
            if form.is_valid():
                form.save()
            return redirect('/Student_SPC/Plist')

@login_required 
def Placements_list(request):
    if'q'in request.GET:
        q=request.GET['q']
        
        multiple_q=Q(Q(Full_name__icontains=q)|Q(Date_of_offer__icontains=q)|Q(Usn__icontains=q)|Q(semester__icontains=q)|Q(Category__icontains=q)|Q(Role__icontains=q)|Q(Company__icontains=q)|Q(Ctc__icontains=q))
        data=Placements.objects.filter(multiple_q).order_by('-Usn') 
    else:
        data=Placements.objects.all().order_by('-Usn')     
    context={'PlacedList':data}
    return render(request,"Placement_list.html",context) 

def Placements_delete(request,id):
    Intern=Placements.objects.get(pk=id)
    Intern.delete()
    return redirect('/Student_SPC/Plist')  

@login_required
def Graduated_form(request,id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id==0:
                form = Graduatedform()
            else:
                G=Graduated.objects.get(pk=id)
                form=Graduatedform(instance=G)    
            return render(request,"Graduated_form.html",{'form':form})
        else:
            if id==0:
                form = Graduatedform(request.POST)
            else:
                G=Graduated.objects.get(pk=id)
                form=Graduatedform(request.POST,instance=G)   
            if form.is_valid():
                form.save()
            return redirect('/Student_SPC/Glist')

@login_required 
def Graduated_list(request):
    if'q'in request.GET:
        q=request.GET['q']
        
        multiple_q=Q(Q(Full_name__icontains=q)|Q(Specialization__icontains=q)|Q(Role__icontains=q)|Q(University__icontains=q)|Q(Current_profile_details__icontains=q))
        data=Graduated.objects.filter(multiple_q)
    else:
        data=Graduated.objects.all()    
    context={'GradList':data}
    return render(request,"Graduated_list.html",context) 

def Graduated_delete(request,id):
    Intern=Graduated.objects.get(pk=id)
    Intern.delete()
    return redirect('/Student_SPC/Glist')  

@login_required
def Unplaced_form(request,id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id==0:
                form = Unplacedform()
            else:
                G=Unplaced.objects.get(pk=id)
                form=Unplacedform(instance=G)    
            return render(request,"Unplaced_form.html",{'form':form})
        else:
            if id==0:
                form = Unplacedform(request.POST)
            else:
                G=Unplaced.objects.get(pk=id)
                form=Unplacedform(request.POST,instance=G)   
            if form.is_valid():
                form.save()
            return redirect('/Student_SPC/Ulist')

@login_required 
def Unplaced_list(request):
    if'q'in request.GET:
        q=request.GET['q']
        
        multiple_q=Q(Q(Full_name__icontains=q)|Q(Usn__icontains=q)|Q(Remarks__icontains=q)|Q(personal_email__icontains=q))
        data=Unplaced.objects.filter(multiple_q)
    else:
        data=Unplaced.objects.all()    
    context={'UList':data}
    return render(request,"Unplaced_list.html",context) 

def Unplaced_delete(request,id):
    Intern=Unplaced.objects.get(pk=id)
    Intern.delete()
    return redirect('/Student_SPC/Ulist')


@login_required
def Drive_form(request,id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id==0:
                form = Driveform()
            else:
                G=Drive.objects.get(pk=id)
                form=Driveform(instance=G)    
            return render(request,"Drive_form.html",{'form':form})
        else:
            if id==0:
                form = Driveform(request.POST)
            else:
                G=Drive.objects.get(pk=id)
                form=Driveform(request.POST,instance=G)   
            if form.is_valid():
                form.save()
            return redirect('/Student_SPC/Dlist')

@login_required 
def Drive_list(request):
    if'q'in request.GET:
        q=request.GET['q']
        
        multiple_q=Q(Q(Full_name__icontains=q)|Q(Usn__icontains=q)|Q(semester__icontains=q)|Q(Company__icontains=q)|Q(Date_of_drive__icontains=q))
        data=Drive.objects.filter(multiple_q).order_by('semester')
    else:
        data=Drive.objects.all().order_by('semester')    
    context={'DList':data}
    return render(request,"Drive_list.html",context) 

def Drive_delete(request,id):
    Intern=Drive.objects.get(pk=id)
    Intern.delete()
    return redirect('/Student_SPC/Dlist')   


class Upload(FormView):
    form_class = UploadForm
    template_name = 'Upload.html'

    def form_valid(self, form):
        status = handle_csv(self.request.FILES["file"])
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('Placed_list')    
    

@login_required
def Shome(request):
    


    return render(request,"Shome.html")
@login_required
def Analysis(request):
    if'q'in request.GET:
        q=request.GET['q']
        n=int(q)
        r=n%100
        r=r-4
        s=str(r)
        res='RV'+s
        
        
       
        data1=Placements.objects.filter(Usn__icontains=res , Category__icontains='Open Dream' ).count()
        data2=Placements.objects.filter(Usn__icontains=res , Category=' Dream' ).count()
        high=Placements.objects.filter(Usn__icontains=res).aggregate(high=Max('Ctc'))
        low=Placements.objects.filter(Usn__icontains=res).aggregate(low=Min('Ctc'))
        avg=Placements.objects.filter(Usn__icontains=res ).aggregate(avg=Avg('Ctc'))
        elig=Placements.objects.filter(Usn__icontains=res).count()
        uelig=Unplaced.objects.filter(Usn__icontains=res,Eligible='Yes').count()
        hs=Unplaced.objects.filter(Usn__icontains=res,Interested_In_higherStudies='Yes').count()
        a=Placements.objects.filter(Usn__icontains=res,Ctc__lte=8).count()
        b=Placements.objects.filter(Usn__icontains=res,Ctc__gte=8,Ctc__lte=15).count()
        c=Placements.objects.filter(Usn__icontains=res,Ctc__gte=15,Ctc__lte=25).count()
        d=Placements.objects.filter(Usn__icontains=res,Ctc__gte=25).count()



    else:
        q=2024
        data1=Placements.objects.filter(Usn__icontains='RV20', Category__icontains='Open Dream' ).count()
        data2=Placements.objects.filter(Usn__icontains='RV20', Category=' Dream' ).count()
        high=Placements.objects.filter(Usn__icontains='RV20').aggregate(high=Max('Ctc'))
        low=Placements.objects.filter(Usn__icontains='RV20').aggregate(low=Min('Ctc'))
        avg=Placements.objects.filter(Usn__icontains='RV20').aggregate(avg=Avg('Ctc'))
        elig=Placements.objects.filter(Usn__icontains='RV20').count()
        uelig=Unplaced.objects.filter(Usn__icontains='RV20',Eligible='Yes').count()
        hs=Unplaced.objects.filter(Usn__icontains='RV20',Interested_In_higherStudies='Yes').count()
        a=Placements.objects.filter(Usn__icontains='RV20',Ctc__lte=8).count()
        b=Placements.objects.filter(Usn__icontains='RV20',Ctc__gte=8,Ctc__lte=15).count()
        c=Placements.objects.filter(Usn__icontains='RV20',Ctc__gte=15,Ctc__lte=25).count()
        d=Placements.objects.filter(Usn__icontains='RV20',Ctc__gte=25).count()


    
    
    context={
        'data1':data1,
        'data2':data2,
        'q':q,
        'high':high,
        'low':low,
        'avg':avg,
        'elig':elig+uelig,
        'placed':elig,
        'hs':hs,
        'a':a,
        'b':b,
        'c':c,
        'd':d,

    }
    return render(request,"Panalysis.html",context)

def Hanalysis(request):
    o1=Placements.objects.filter(Usn__icontains='RV17').count()
    o2=Placements.objects.filter(Usn__icontains='RV18').count()
    o3=Placements.objects.filter(Usn__icontains='RV19').count()
    o4=Placements.objects.filter(Usn__icontains='RV20').count()
    
    l1=Placements.objects.filter(Usn__icontains='RV17').aggregate(l1=Min('Ctc'))
    l2=Placements.objects.filter(Usn__icontains='RV18').aggregate(l2=Min('Ctc'))
    l3=Placements.objects.filter(Usn__icontains='RV19').aggregate(l3=Min('Ctc'))
    l4=Placements.objects.filter(Usn__icontains='RV20').aggregate(l4=Min('Ctc'))
    a=Placements.objects.filter(Usn__icontains='RV17').aggregate(a=Max('Ctc'))
    b=Placements.objects.filter(Usn__icontains='RV18').aggregate(b=Max('Ctc'))
    c=Placements.objects.filter(Usn__icontains='RV19').aggregate(c=Max('Ctc'))
    d=Placements.objects.filter(Usn__icontains='RV20').aggregate(d=Max('Ctc'))
    a1=Placements.objects.filter(Usn__icontains='RV17').aggregate(a1=Avg('Ctc'))
    a2=Placements.objects.filter(Usn__icontains='RV18').aggregate(a2=Avg('Ctc'))
    a3=Placements.objects.filter(Usn__icontains='RV19').aggregate(a3=Avg('Ctc'))
    a4=Placements.objects.filter(Usn__icontains='RV20').aggregate(a4=Avg('Ctc'))
    context={
        'o1':o1,
        'o2':o2,
        'o3':o3,
        'o4':o4,
        'l1':l1,
        'l2':l2,
        'l3':l3,
        'l4':l4,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'a1':a1,
        'a2':a2,
        'a3':a3,
        'a4':a4,
        

    }

    return render(request,'Hanalysis.html',context)
def Ianalysis(request):
    if'q'in request.GET:
        q=request.GET['q']
        n=int(q)
        r=n%100
        r=r-4
        s=str(r)
        res='RV'+s
        i=Internship.objects.filter(Usn__icontains=res ).count()
        on=Internship.objects.filter(Usn__icontains=res,Type=' On Campus' ).count()
        off=Internship.objects.filter(Usn__icontains=res,Type=' Off Campus' ).count()
    else:
        q=2024    
        i=Internship.objects.filter(Usn__icontains='RV20' ).count()
        on=Internship.objects.filter(Usn__icontains='RV20',Type=' On Campus' ).count()
        off=Internship.objects.filter(Usn__icontains='RV20',Type=' Off Campus' ).count()
    context={
        'i':i,
        'on':on,
        'off':off,
        'q':q,
    }    



    
    return render(request,'Ianalysis.html',context)


def Email(request):
        connection = mail.get_connection()

# Manually open the connection
        connection.open()
    
        html_template = 'email_template.html'
        data=Drive.objects.filter( Date_of_drive__gte=datetime.now() - timedelta(days=7),semester=5)    
        context1={'DList':data}
        data1=Drive.objects.filter( Date_of_drive__gte=datetime.now() - timedelta(days=7),semester=6)    
        context2={'DList':data1}
        data3=Drive.objects.filter( Date_of_drive__gte=datetime.now() - timedelta(days=7),semester=7)    
        context3={'DList':data3}
        data4=Drive.objects.filter( Date_of_drive__gte=datetime.now() - timedelta(days=7),semester=8)    
        context4={'DList':data4}


        html_message1 = render_to_string(html_template,context1 )
        html_message2 = render_to_string(html_template,context2 )
        
        html_message3 = render_to_string(html_template,context3 )
        html_message4 = render_to_string(html_template,context4 )
        email5=Faculty.objects.values_list('email',flat=True).filter(semester=5)
        email7=Faculty.objects.values_list('email',flat=True).filter(semester=7)
        email6=Faculty.objects.values_list('email',flat=True).filter(semester=6)
        email8=Faculty.objects.values_list('email',flat=True).filter(semester=8)


        message1 = EmailMessage('django', html_message1,'djangomailtemp@gmail.com',email5
        )
        message2 = EmailMessage('django', html_message2,'djangomailtemp@gmail.com',email6
        )
        message3 = EmailMessage('django', html_message3,'djangomailtemp@gmail.com',email7
        )
        message4 = EmailMessage('django', html_message4,'djangomailtemp@gmail.com',email8
        )
        message1.content_subtype = 'html' # this is required because there is no plain text email message
        message2.content_subtype='html'
        message3.content_subtype='html'
        message4.content_subtype='html'
        connection.send_messages([message1, message2,message3,message4])

        connection.close()
        
    
   
    

        return render(request,'email_succ.html')