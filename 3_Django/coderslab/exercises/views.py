from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import SCHOOL_CLASS, Student

# Create your views here.
class SchoolView(View):

    def get(self, request):
        html = """<!doctype html>

<html>
    <head><meta charset="utf-8"></head>
    <body>
        <h1>Szkoła podstawowa nr 1 im. Chucka Norrisa.</h1>
        <h2>Klasy:</h2>
        <ul>
            {}
        </ul>
    </body>
</html>
"""
        class_list = []
        for school_class in SCHOOL_CLASS:
            class_list.append("<li><a href='/class/{}'>{}</a></li>".format(school_class[0], school_class[1]))
        classes_part = "".join(class_list)
        return HttpResponse(html.format(classes_part))


class SchoolClassView(View):

    def get(self, request, school_class):
        students = Student.objects.filter(school_class=school_class)
        return render(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(school_class)][1]})