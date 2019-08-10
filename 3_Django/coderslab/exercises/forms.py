from django import forms
from .models import GRADES, Student, SchoolSubject, StudentGrades, Toppings, Pizza, EXCHANGE
from .models import PIZZA_SIZES, PresenceList, SCHOOL_CLASS, BACKGROUND
from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError

class StudentSearchForm(forms.Form):
    last_name = forms.CharField(label="Podaj nazwisko", max_length=15)

# dzien 2 / 2 formularze / zad 2 i 3
class StudentAddForm(forms.Form):
    first_name = forms.CharField(label="Wpisz imię:", max_length=20)
    last_name = forms.CharField(label="Wpisz nazwisko:", max_length=30)
    # year_of birth = forms.IntegerField(label="Wpisz rok urodzenia:")
    school_class = forms.ChoiceField(choices=SCHOOL_CLASS)

# dzien 2 / 2 formularze / zad 4
class ExchangeForm(forms.Form):
    currency1 = forms.DecimalField(label="Kwota PLN:", max_digits=6, decimal_places=2)
    currency2 = forms.DecimalField(label="Kwota USD:", max_digits=6, decimal_places=2)
    conversion = forms.ChoiceField(choices=EXCHANGE)

class StudentSubjectGradeForm(forms.Form):
    last_name = forms.ChoiceField(choices=((s.id, s.last_name) for s in Student.objects.all()))
    subject = forms.ChoiceField(choices=((s.id, s.name) for s in SchoolSubject.objects.all()))
    grade = forms.ChoiceField(choices=GRADES)

# dzien 2 / 3 Widgety / zad 1
class ComposePizzaForm(forms.Form):
    topping = forms.ModelMultipleChoiceField(queryset=Toppings.objects.all())

# dzien 2 / 3 Widgety / zad 2
class StudentPresenceListForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.order_by('-last_name'))
    day = forms.DateField(widget=forms.HiddenInput)
    present = forms.BooleanField(label="Obecny")

# dzien 2 / 3 widgety / zad 3
class SetColorForm(forms.Form):
    background_color = forms.ChoiceField(widget=forms.RadioSelect, choices=BACKGROUND)

# dzien 2 / 3 widgety / zad 4
class LoginForm(forms.Form): 
    login = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, max_length=10)

# d2 -4 -zad 1 

def validate_two_dots(value):
    if value.count('.') <2:
        raise ValidationError("za malo kropeczek")

class ErrorValidationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField(validators = [EmailValidator()])
    # email = forms.EmailField() działa walidacja
    www = forms.CharField(validators= [validate_two_dots, URLValidator()])
    # www = forms.URLField() nie działa walidacja/inna walidacja


class SchoolSubjectModelForm(forms.ModelForm):
    class Meta:
        model = SchoolSubject
        fields = '__all__'
