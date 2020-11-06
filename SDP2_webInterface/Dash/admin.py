from django.contrib import admin
from .models import DashPanelData, PrintTrackData

class DashPanelDataAdmin(admin.ModelAdmin):
    list_display = (
        'file_name',
        'type_of_print',
        'time_of_print_start',
        'time_of_print_finish',
    )


class PrintTrackDataAdmin(admin.ModelAdmin):
    list_display = (
        'number_of_jobs',
        'Undergoing_jobs',
        'successful_prints',
        'error_prints',
    )
    def has_add_permission(self, request): 
        return False


admin.site.register(DashPanelData,DashPanelDataAdmin )
admin.site.register(PrintTrackData, PrintTrackDataAdmin)
