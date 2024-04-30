
from django import forms
from django.forms import DateInput, EmailInput, PasswordInput, RadioSelect, Select, URLInput
from .models import User
import re

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'