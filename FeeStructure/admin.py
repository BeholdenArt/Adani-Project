from django.contrib import admin
from FeeStructure.models import FeeFormat
# Register your models here.

# admin.site.register(FeeFormat)


@admin.register(FeeFormat)
class FeeFormat(admin.ModelAdmin):
    readonly_fields = ('created_on', 'last_modified')
    list_display = ('receipt_number','received_sum','date','enrolment_number','semester','stream',)
    list_filter = ("semester", "stream")