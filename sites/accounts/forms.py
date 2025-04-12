from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email')
        model = User
    
    def check_password(self):
        cd = self.changed_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Vos mots de passes sont incorrectes')