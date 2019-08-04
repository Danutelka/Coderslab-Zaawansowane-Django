from django import forms
from .models import GRADES, Student, SchoolSubject, StudentGrades, Toppings, Pizza, PIZZA_SIZES, PresenceList
from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError
class StudentSearchForm(forms.Form):
    last_name = forms.CharField(label="Podaj nazwisko", max_length=15)

class StudentSubjectGradeForm(forms.Form):
    last_name = forms.ChoiceField(choices=((s.id, s.last_name) for s in Student.objects.all()))
    subject = forms.ChoiceField(choices=((s.id, s.name) for s in SchoolSubject.objects.all()))
    grade = forms.ChoiceField(choices=GRADES)

class ComposePizzaForm(forms.Form):
    topping = forms.ModelMultipleChoiceField(queryset=Toppings.objects.all())

class StudentPresenceListForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.order_by('-last_name'))
    day = forms.DateField(widget=forms.HiddenInput)
    present = forms.BooleanField(label="Obecny")

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
