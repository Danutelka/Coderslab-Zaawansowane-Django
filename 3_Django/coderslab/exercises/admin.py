from django.contrib import admin
from exercises.models import SchoolSubject, Student, StudentGrades,  \
    PresenceList, Message, StudentNotice

# Register your models here.
admin.site.register(SchoolSubject)
admin.site.register(Student)
admin.site.register(StudentGrades)
admin.site.register(PresenceList)
admin.site.register(Message)
admin.site.register(StudentNotice)