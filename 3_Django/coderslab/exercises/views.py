from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades
from .forms import StudentSearchForm, StudentSubjectGradeForm, ComposePizzaForm
from .models import PIZZA_SIZES, Pizza, Toppings

# Create your views here.
class SchoolView(View):
    def get(self, request):
        crx ={
            "klasy" : SCHOOL_CLASS
        }
        return TemplateResponse(request, "school.html", crx)
class SchoolClassView(View):
    def get(self, request, pk):
        students = Student.objects.filter(school_class=pk)
        return TemplateResponse(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(pk)][1]})
class StudentView(View):
    def get (self, request, pk):
        student = get_object_or_404(Student, id=pk)
        subjects = SchoolSubject.objects.all()
        crx = {
            "s" : student, 
            "subjects" : subjects,
            "school_class" : SCHOOL_CLASS[student.school_class][1]
        }
        return TemplateResponse(request, "student.html", crx)
class GradesView(View):
    def get(self, request, pk, pk2):
        student = get_object_or_404(Student, id=pk)
        subject = get_object_or_404(SchoolSubject, id=pk2)
        grades = StudentGrades.objects.filter(student=student).filter(school_subject=subject)
        average = 0
        if grades.count() > 0:
            average = sum(x.grade for x in grades) / grades.count()
        crx = {
            'student': student,
            'subject': subject,
            'grades': grades,
            'average': average
        }
        return TemplateResponse (request, 'grades.html', crx)

# dzien2/2/zad1

class StudentSearchView2(View):
    def get(self, request):
        context = {
            'form': StudentSearchForm()
        }
        return TemplateResponse (request, "student_search.html", context=context)

    def post(self, request):
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            students = Student.objects.filter(last_name__icontains=last_name)
            context = {
                'form': form,
                'students': students
            }
        return TemplateResponse(request, "student_search.html", context=context)


class StudentSearchView(View):
    def get(self, request):
        context = {
            'form': StudentSearchForm()
        }
        return TemplateResponse(request, "student_search.html", context=context)
    def post(self, request):
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name'] #pobiera sprawdzone dane --> cleaned_data
            students = Student.objects.filter(last_name__icontains=last_name) #wybiera z bazy danych
            context = {
                'form': form,
                'students': students,
            }
            return TemplateResponse(request, "student_search.html", context=context)

# zad 5
class AddGradeView(View):
    def get(self, request):
        form = StudentSubjectGradeForm()
        return TemplateResponse(request, "add_grades.html", {'form':form})
    def post(self, request):
        form = StudentSubjectGradeForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['last_name']
            subject_id = form.cleaned_data['subject']
            grade = form.cleaned_data['grade']
            student = Student.objects.get(id=student_id)
            subject = SchoolSubject.objects.get(id=subject_id)
            StudentGrades.objects.create(student=student, school_subject=subject, grade=grade)
             # return HttpResponseRedirect("student") --- nie ma takiego urls
            return HttpResponse(f"""
                <p>student_id = {student_id}</p>
                <p>subject_id = {subject_id}</p>
                <p>grade = {grade}</p>
            """)

class ComposePizzaView(View):
    def get(self, request):
        form = ComposePizzaForm()
        return render(request, 'compose_pizza.html', context={'form': form})