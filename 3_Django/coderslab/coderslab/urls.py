"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.urls import re_path
from django.contrib import admin

from exercises.views import SchoolView, SchoolClassView, StudentView, GradesView, SchoolSubjectFormView
from exercises.views import StudentSearchView, AddGradeView, ComposePizzaView, PresenceListView, D2P3E1View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SchoolView.as_view(), name="index"),
    path('class/<int:pk>', SchoolClassView.as_view(), name="school-class"),
    path('student/<int:pk>', StudentView.as_view(), name="student"),
    path('student/<int:pk>/<int:pk2>', GradesView.as_view(), name="grades"),
    path('student_search', StudentSearchView.as_view(), name="student_search"),
    path('add_grade', AddGradeView.as_view(), name="add_grade"),
    path('pizza', ComposePizzaView.as_view(), name="pizza"),
    path('class_presence/<int:student_id>/<str:day>', PresenceListView.as_view(), name="presence-list"),
    path('d2_p3_e3', D2P3E1View.as_view(), name="d2_p3_e3"),
    path('dodaj_przedmiot', SchoolSubjectFormView.as_view, name="dodaj_przedmiot"),
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', SchoolView.as_view(), name="index"),
    # url(r'^class/(?P<school_class>(\d)+)', SchoolClassView.as_view(), 
    #    name="school-class" )
]
