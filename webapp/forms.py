
from django import forms


class ContactForms(forms.Form):
    first_name = forms.CharField(required=False, max_length=100, help_text='100 characters max.')
    last_name = forms.CharField(required=False, max_length=100, help_text='100 characters max.')
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=14)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    location = forms.CharField(required=True, max_length=300, help_text='Enter your location')
