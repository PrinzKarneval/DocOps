from django.contrib import admin

from patients.models import Patient, Label, Insurance


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email']
    list_filter = ['last_name']
    search_fields = ['last_name']
