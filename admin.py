from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register (Biodata)
admin.site.register (Country)
admin.site.register (Gender)
admin.site.register (SalaryScale)
admin.site.register (Directorate)
admin.site.register (Signatory)
admin.site.register (Department)
admin.site.register (Unit)
admin.site.register (SubUnit)
admin.site.register (EmploymentDetails)


