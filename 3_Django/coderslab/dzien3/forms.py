from django import forms
from django.contrib.auth.models import User
from django.core.validators import URLValidator, EmailValidator

#zad2

#class UserModelForm(forms.modelForm):
#    class Meta:
#       model = User
#       fields=('username', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(label="wpisz nazwę użytkownika")
    password = forms.CharField(widget=forms.PasswordInput(), label="wpisz hasło")

# zad 3
def validate_username(value):
    if value == "a":
        raise ValidationError("Taki username istnieje")

class AddUserForm(forms.Form):
    username = forms.CharField(validators=[validate_username], label="wpisz login", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput(), label="wpisz hasło", max_length=64)
    password_again = forms.CharField(widget=forms.PasswordInput(), label="wpisz ponownie hasło")
    first_name = forms.CharField(label="wpisz imię", max_length=64)
    last_name = forms.CharField(label="wpisz nazwisko", max_length=64)
    email = forms.CharField(validators=[EmailValidator()])

# zad 4 
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(), label="wprowadź nowe hasło")
    new2_password = forms.CharField(widget=forms.PasswordInput(), label="wprowadź stare hasło")
