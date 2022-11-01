from django.contrib import admin

from bill.models import Invoice, Organization, PaymentItem


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentItem)
class PaymentItemAdmin(admin.ModelAdmin):
    pass
