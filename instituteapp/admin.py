from django.contrib import admin
from instituteapp.models import ServicerData
class ServicerDataAdmin(admin.ModelAdmin):
    list_display = ['courseno',
                    'coursename',
                    'fee',
                    'faculty',
                    'timeduration']

admin.site.register(ServicerData,ServicerDataAdmin)
