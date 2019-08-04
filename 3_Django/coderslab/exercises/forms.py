from django import forms
from .models import GRADES, Student, SchoolSubject, StudentGrades, Toppings, Pizza, PIZZA_SIZES

class StudentSearchForm(forms.Form):
    last_name = forms.CharField(label="Podaj nazwisko", max_length=15)

class StudentSubjectGradeForm(forms.Form):
    last_name = forms.ChoiceField(choices=((s.id, s.last_name) for s in Student.objects.all()))
    subject = forms.ChoiceField(choices=((s.id, s.name) for s in SchoolSubject.objects.all()))
    grade = forms.ChoiceField(choices=GRADES)

class ComposePizzaForm(forms.Form):
    topping = forms.MultipleChoiceField(choices=(
        (t.id, t.name) for t in Toppings.objects.all()
        )
    )