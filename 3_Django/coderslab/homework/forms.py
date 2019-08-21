from django import forms
from django.forms import ModelForm
from .models import Category, Product, VAT

# dzien2 / zad 5
class AddCategoryForm(forms.Form):
    category_name = forms.CharField(label="Wpisz nazwę nowej kategorii:", max_length=64)
    slug = forms.CharField(label="Określ slug:", max_length=64)

class EditCategoryForm(forms.Form):
    category_name = forms.CharField(label="Edytuj nazwę kategorii:", max_length=64)
    slug = forms.CharField(label="Edytuj slug:", max_length=64)

# dzien 2 / zad 6
class EditProductForm(forms.Form):
    name = forms.CharField(label="Edytuj nazwę produktu:", max_length=128)
    description = forms.CharField(label="Edytuj opis produktu:")
    price = forms.DecimalField(label="Edytuj cenę:", max_digits=6, decimal_places=2)
    vat = forms.ChoiceField(label="Edytuj VAT:", choices=VAT)
    stock = forms.IntegerField(label="Edytuj ilosć w magazynie:")
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

# dzien 2 / zad 7*
class SearchForm(forms.Form):
    name = forms.CharField(label="wyszukaj")

# dzien 3 / zad 8
class LoginForm(forms.Form): 
    login = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, max_length=10)

