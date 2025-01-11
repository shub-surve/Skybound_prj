from django import forms
from intl_tel_input.widgets import IntlTelInputWidget
from .models import UserDetails

class GetDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'phone_no']  # Exclude 'event'
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control'
            }),
            'phone_no': IntlTelInputWidget(attrs={
                'class': 'form-control',
                'required': 'false'
            }),
        }
