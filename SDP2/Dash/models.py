from django.db import models


class DashPanelData(models.Model):
    time_of_print_start     = models.DateTimeField(auto_now_add=False)
    time_of_print_finish    = models.DateTimeField()
    total_print_time        = models.IntegerField()
    type_of_print           = models.CharField(max_length=20)
    machine_state           = models.CharField(max_length=15)
    file_name               = models.CharField(max_length=255)
    tool_installed          = models.CharField(max_length=50)

class PrintTrackData(models.Model):
    number_of_jobs          = models.IntegerField(default= 0)
    Undergoing_jobs         = models.IntegerField(default= 0)
    successful_prints       = models.IntegerField(default= 0)
    error_prints            = models.IntegerField(default= 0)


