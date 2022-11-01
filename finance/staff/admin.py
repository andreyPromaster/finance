from django.contrib import admin

from staff.models import Employee, Company, BankDetails


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(BankDetails)
class BankDetailsAdmin(admin.ModelAdmin):
    pass
