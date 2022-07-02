from dataclasses import field
from django.forms import ModelForm
from .models import email,OTP

class ProjectForm(ModelForm):
    class Meta:
        model =  email
        fields = '__all__'

class OTPForm(ModelForm):
    class Meta:
        model = OTP
        fields = '__all__'