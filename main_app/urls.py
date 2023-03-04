
from django.urls import path,include
from .import views
from .views import Upload
urlpatterns = [
    path('form/', views.Internship_form,name='Intern_form'),
    path('form/<int:id>', views.Internship_form,name='Internupdate'),
    path('list/',views.Internship_list,name='Intern_list'),
    path('delete/<int:id>/',views.Internship_delete,name='Interndel'), 
    path('Plist/',views.Placements_list,name='Placed_list'), 
    path('Pform/', views.Placements_form,name='Placed_form'),
    path('Pform/<int:id>', views.Placements_form,name='Placedupdate'),
    path('Pdelete/<int:id>/',views.Placements_delete,name='Placeddel'),
    path('Glist/',views.Graduated_list,name='Grad_list'), 
    path('Gform/', views.Graduated_form,name='Grad_form'),
    path('Gform/<int:id>', views.Graduated_form,name='Gradupdate'),
    path('Gdelete/<int:id>/',views.Graduated_delete,name='Graddel'),
    path('Ulist/',views.Unplaced_list,name='Ulist'), 
    path('Uform/', views.Unplaced_form,name='Uform'),
    path('Uform/<int:id>', views.Unplaced_form,name='Uupdate'),
    path('Udelete/<int:id>/',views.Unplaced_delete,name='Udel'),
    path('Dlist/',views.Drive_list,name='Dlist'), 
    path('Dform/', views.Drive_form,name='Dform'),
    path('Dform/<int:id>', views.Drive_form,name='Dupdate'),
    path('Ddelete/<int:id>/',views.Drive_delete,name='Ddel'), 
    path('Shome/',views.Shome,name='Shome'), 
    path('Upload',Upload.as_view(),name='upload'),
    path('Panalysis/',views.Analysis,name='Panalysis'),
     path('Hanalysis/',views.Hanalysis,name='Hanalysis'),
     path('Ianalysis/',views.Ianalysis,name='Ianalysis'),
     path('Email',views.Email,name='Email'),


     


    


]
