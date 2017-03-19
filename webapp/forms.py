from django import forms


class ContactForms(forms.Form):
    first_name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
    last_name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
    user_name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    phone_number = forms.CharField(required=True, max_length=14)
    location = forms.CharField(required=True, max_length=300, help_text='Enter your location')


class LoginForms(forms.Form):
    user_name = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class OrdersForms(forms.Form):
    proxy_first_name = forms.CharField(required=False, max_length=100, help_text='enter your proxy first name')
    proxy_last_name = forms.CharField(required=False, max_length=100, help_text='enter your proxy last name')
    proxy_phone_number = forms.CharField(required=False, max_length=100, help_text='enter your proxy phone number')
    is_registered_to_kongapay = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Paying with Konga Pay?')
