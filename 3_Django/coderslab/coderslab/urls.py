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

from exercises.views import SchoolView, SchoolClassView, StudentView, GradesView
from exercises.views import SchoolSubjectFormView, StudentAddView, LoginView
from exercises.views import StudentSearchView, AddGradeView, ComposePizzaView
from exercises.views import PresenceListView, SetColorView, ExchangeView
from exercises.views import D2P3E1View, D2P3E3View, D2P3E4View, MessageCompose, \
StudentNoticeView, NoticeCreate, NoticeDelete, NoticesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SchoolView.as_view(), name="index"),
    path('class/<int:pk>', SchoolClassView.as_view(), name="school-class"),
    path('student/<int:pk>', StudentView.as_view(), name="student"),
    path('student/<int:pk>/<int:pk2>', GradesView.as_view(), name="grades"),
    path('student_search', StudentSearchView.as_view(), name="student_search"),
    path('add_grade', AddGradeView.as_view(), name="add_grade"),
    path('add_student', StudentAddView.as_view(), name="add_student"),
    path('pizza', ComposePizzaView.as_view(), name="pizza"),
    path('exchange', ExchangeView.as_view(), name="exchange"),
    path('class_presence/<int:student_id>/<str:day>', PresenceListView.as_view(), name="presence-list"),
    path('login', LoginView.as_view(), name="login"),
    path('set_color', SetColorView.as_view(), name="background_color"),
    path('d2_p3_e1', D2P3E1View.as_view(), name="d2_p3_e1"),
    path('d2_p3_e3', D2P3E3View.as_view(), name="d2_p3_e3"),
    path('d2_p3_e4', D2P3E4View.as_view(), name="d2_p3_e4"),
    path('dodaj_przedmiot', SchoolSubjectFormView.as_view, name="dodaj_przedmiot"),
    path('compose_message', MessageCompose.as_view(), name="compose_message"),
    path('notices/<int:pk>', StudentNoticeView.as_view(), name="students_notes"),
    path('notice_add', NoticeCreate.as_view(), name="add_notice"),
    path('notice_del/<int:pk>', NoticeDelete.as_view(), name="delete_notice"),
    path('notices_all', NoticesView.as_view(), name="notices")
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', SchoolView.as_view(), name="index"),
    # url(r'^class/(?P<school_class>(\d)+)', SchoolClassView.as_view(), 
    #    name="school-class" )
]
