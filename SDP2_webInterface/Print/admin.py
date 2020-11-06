from django.contrib import admin
from .models import PrintFile

class PrintFileAdmin(admin.ModelAdmin):
    list_display = (
        'print_file',
        'is_print_cnc',
        'is_print_3d',
        'is_print_file_gcode',
    )

admin.site.register(PrintFile, PrintFileAdmin)

