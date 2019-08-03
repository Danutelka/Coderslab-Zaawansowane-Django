from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades
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




