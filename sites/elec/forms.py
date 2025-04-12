from django import forms
from django.contrib.auth.models import User
from .models import Product, Profile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']