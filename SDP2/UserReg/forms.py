from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.core.exceptions import ValidationError


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
                required=True,
                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Enter your username",
                                        "class": "form-control py-4",
                                        "id": "inputFirstName",
                                        "type":"text"
                                        
                                        
                                    }     
                                ))
    first_name = forms.CharField(
                required=True,
                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Enter your First name",
                                        "class": "form-control py-4",
                                        "id": "inputFirstName",
                                        "type":"text"
                                        
                                    }     
                                ))
    last_name = forms.CharField(
                required=True,
                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Enter your Last name",
                                        "class": "form-control py-4",
                                        "id": "inputLastName",
                                        "type":"text"
                                    }     
                                ))
    email = forms.CharField(
                required=True,
                widget=forms.EmailInput(
                                    attrs={
                                        "placeholder": "Enter email address",
                                        "class": "form-control py-4",
                                        "id": "inputEmailAddress",
                                    }     
                                ))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(
                                    attrs={
                                        "placeholder": "Enter password",
                                        "class": "form-control py-4",
                                        "id": "inputPassword",
                                        "type":"password",
                                    }
    ))
    password2 = forms.CharField(required=True, label='Password confirmation', widget=forms.PasswordInput(
                                    attrs={
                                        "placeholder": "Confirm password",
                                        "class": "form-control py-4",
                                        "id": "inputConfirmPassword",
                                        "type":"password",
                                    }
    ))        
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2