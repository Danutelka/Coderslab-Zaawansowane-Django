from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from .forms import SchoolSubjectModelForm, StudentAddForm, SetColorForm
from django.shortcuts import get_object_or_404
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades, EXCHANGE, Message, StudentNotice
from .forms import StudentSearchForm, StudentSubjectGradeForm, ComposePizzaForm, LoginForm,  \
StudentPresenceListForm, ErrorValidationForm, SchoolSubjectModelForm, StudentNoticeForm
from .forms import ExchangeForm, Error2ValidationForm, Error3ValidationForm
from .models import PIZZA_SIZES, Pizza, Toppings, PresenceList

# Create your views here.

# dzien 1 / zad 2
class SchoolView(View):
    def get(self, request):
        crx ={
            "klasy" : SCHOOL_CLASS
        }
        return TemplateResponse(request, "school.html", crx)

# dzien 1 / zad 3
class SchoolClassView(View):
    def get(self, request, pk):
        students = Student.objects.filter(school_class=pk)
        return TemplateResponse(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(pk)][1]})
# dzien 1 / zad 4 
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

# dzien 1 / zad 5
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

# dzien2 / 2 Formularze / zad1
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

# dzien 2 / 2 Formularze / zad2, zad3
class StudentAddView(View):
    def get (self, request):
        form = StudentAddForm()
        return TemplateResponse(request, "add_student.html", {'form': form})
    def post (self, request):
        form = StudentAddForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            #year_of_birth = form.cleaned_data['year_of_birth']
            school_class = form.cleaned_data['school_class']
            Student.objects.create(first_name=first_name, last_name=last_name, school_class=school_class)
            return HttpResponse("Dodano")

# dzien 2/ 2 formularze / zad 4
class ExchangeView(View):
    def get(self, reguest):
        form = ExchangeForm()
        return TemplateResponse(reguest, "exchange.html", {'form': form})
    def post(self, request):
        form = ExchangeForm(request.POST)
        if form.is_valid():
            currency = form.cleaned_data['currency']
            conversion = form.cleaned_data['conversion']
            if int(conversion == 1):
                wynik = (currency1) * 3.9
                return wynik
            else:
                wynik = int(currency2) / 3.9
                return wynik
            return render(wynik)


# dzien 2/ 2 formularze / zad 5
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

# dzien 2 / 3 Widgety / zad 1
class ComposePizzaView(View):
    def get(self, request):
        form = ComposePizzaForm()
        return render(request, 'compose_pizza.html', context={'form': form})

# dzien 2 / 3 Widgety / zad 2
class PresenceListView(View):
    def get(self, request, student_id, day):
        student = Student.objects.get(id=student_id)
        form = StudentPresenceListForm(initial= {
            'day': day,
            'student': student
        })
        return render(request, 'presence.html', context={'form': form})
    
    def post(self, request, student_id, day):
        student = Student.objects.get(id=student_id)
        form = StudentPresenceListForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            student = form.cleaned_data['student']
            present = form.cleaned_data['present']
            PresenceList.objects.create(student=student, present=present, day=day)
            return HttpResponse("day= {} student= {} present = {}" .format(day, student, present))
        else:
            return HttpResponse("{}" .format(str(form.errors)))

# dzien 2 / 3 widgety / zad3
class SetColorView(View):
    def get (self, request):
        form = SetColorForm()
        return TemplateResponse(request, "set_color.html", {'form': form})
    def post (self, request):
        form = SetColorForm(request.POST)
        if form.is_valid():
            color = form.cleaned_data['background_color']
            return TemplateResponse(request, "set_color.html", {'form': form, 'background_color': color})

# dzien 2 / 3 Widgety / zad4
class LoginView(View):
    def get(self, request):
        context = {
            'form': LoginForm()
            }
        return TemplateResponse(request, "login.html", context=context)
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            if (login == "root") and (password == "very_secret"):
                return HttpResponse("Miło Cię widzieć")
            else:
                return HttpResponse("A sio, hakerze !!!")

# dzien 2 /4 Obsługa błędów / zad 1 
class D2P3E1View(View):
    def get(self, request):
        form = ErrorValidationForm()
        return render(request, 'd2_p3_e1.html', context={'form': form})

    def post(self, request):
        form = ErrorValidationForm(request.POST)
        if form.is_valid():
            return HttpResponse("wszystko ok")
        else:
            return render(request, "form_errors.html", context={'form': form})

# dzien 2 /4 Obsługa błędów / zad 3
class D2P3E3View(View):
    def get(self, request):
        form = Error2ValidationForm()
        return TemplateResponse(request, 'd2_p3_e3.html', context={'form': form})

    def post(self, request):
        form = Error2ValidationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Facet")
        else:
            # return HttpResponse("Babka")
            return render(request, "form2_errors.html", context={'form': form})

# dzien 2 /4 Obsługa błędów / zad 4
class D2P3E4View(View):
    def get(self, request):
        form = Error3ValidationForm()
        return TemplateResponse(request, 'd2_p3_e4.html', context={'form': form})
    def post(self, request):
        form = Error3ValidationForm(request.POST)
        if form.is_valid():
            return HttpResponse("OK")
        else:
            return render(request, "form3_errors.html", context={'form': form})

class SchoolSubjectFormView(FormView):
    form_class = SchoolSubjectModelForm
    # template_name  'school_subject_form.html'

# dzien 2/ 5 ModelForm / zad 2
class MessageCompose(CreateView):
    model = Message
    fields = '__all__'
    success_url = "compose_message"
    #form_class = MessageForm
    #template_name = 'message.html'
    #success_url = 'compose_message'
   
# dzien 2 / 5 ModelForm / zad 3
class StudentNoticeView(View):
    def get(self, request, pk):
        student = Student.objects.get(id=pk)
        notice = StudentNotice.objects.filter(to=student)
        return render(request, 'notice.html', context={'student': student, 'notice': notice, })

# dzien 2 / 5 ModelForm / zad 4
class NoticeCreate(CreateView):
    model = StudentNotice
    fields = '__all__'
    success_url = "notice_add"

class NoticeDelete(DeleteView):
    model = StudentNotice
    success_url = 'notices_all'
    #def post(self, request, pk):
     #   x = Notice.objects.filter(id=pk)
      #  return render(request, 'exercises/notice_confirm_delete.html', context={'x': x})

class NoticesView(View):
    def get (self, request):
        notices = StudentNotice.objects.all()
        crx = {
            "od" : od, 
            "to" : to,
            "content" : content
            }
        return TemplateResponse(request, "notices.html", crx)
