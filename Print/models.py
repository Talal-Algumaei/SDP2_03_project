from django.db import models


class PrintFile(models.Model):
    print_file = models.FileField(blank=False, null=False)
    is_print_cnc = models.BooleanField(default=False, blank=False)
    is_print_3d = models.BooleanField(default=False,blank=False)
    is_print_file_gcode = models.BooleanField(default=False,blank=False)
    is_tool_installed = models.BooleanField(default=False,blank=False)

    