from django.forms import ModelForm
from .models import PrintFile
from django import forms


class NewPrintForm(ModelForm):
    print_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':"upload-input"}))
    is_print_cnc = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"checkboxIM"}), required=False)
    is_print_3d = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"checkboxIM"}), required=False)
    is_print_file_gcode = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"checkboxIM"}), required=False)
    is_tool_installed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"checkboxIM"}), required=False)
    
    class Meta:
        model = PrintFile
        fields = [
            'print_file',
            'is_print_cnc',
            'is_print_3d',
            'is_print_file_gcode',
            'is_tool_installed',
        ]