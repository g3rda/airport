from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))  
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        widgets = {
        'username' : forms.TextInput(attrs={'class' : 'form-control'})
        } 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']