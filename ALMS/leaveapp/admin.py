from django.contrib import admin

from leaveapp.models import Department, Directorate, EmploymentDetails, SubUnit, Unit

# Register your models here.
admin.site.register(Directorate)
admin.site.register(Department)
admin.site.register(Unit)
admin.site.register(SubUnit)
admin.site.register(EmploymentDetails)

