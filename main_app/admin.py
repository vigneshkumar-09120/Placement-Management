from django.contrib import admin
from .models import Internship , Drive,Unplaced,Placements,Graduated,Document,Faculty

# Register your models here.
admin.site.register(Internship)
admin.site.register(Drive)
admin.site.register(Unplaced)
admin.site.register(Placements)
admin.site.register(Graduated)
admin.site.register(Document)
admin.site.register(Faculty)
