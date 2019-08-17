from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, AddUserForm, ResetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import django.contrib.auth.decorators
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

# zad 1
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "dzien3/user_list.html", context={
            'users': users
        })

# zad 2
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'dzien3/login.html', context={'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.values()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('zalogowany')
            else:
                return HttpResponse('ups niepoprawne logowanie')
        return render(request, 'dzien3/login.html', context={'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')

# zad 3
class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'dzien3/add_user.html', context={'form':form})
    def post(self,request):
        form = AddUserForm(request.POST)
        error = []
        if form.is_valid():
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if not User.objects.filter(username=username).exists():
                if password == password_again:
                    User.objects.create_user(username, password, first_name=first_name, last_name=last_name)
                    return HttpResponseRedirect("list_users/")
                else:
                    error.append('Hasła są różne')
            else:
                error.append('użytkownik isnieje')
        return render(request, 'html', cotext={'form':form, 'error':error})

# zad 4 
class ResetPasswordView(PermissionRequiredMixin, View):
    permission_required = 'auth.change_user'
    #permission_required = 'cms.publish_homepage'
    def get(self, request, p):
        form = ResetPasswordForm()
        # us=request.user()
        us = User.objects.get(id=p)
        return render(request, 'dzien3/reset_password.html', context={'form': form, 'us': us})
    def post(self, request, p):
        form = ResetPasswordForm(request.POST)
        us = User.objects.get(id=p)
        if form.is_valid():
            us.new_password = form.cleaned_data['new_password']
            us.new2_password = form.cleaned_data['new2_password']
            if us.new_password == us.new2_password:
                us.set_password(request.POST.get('new_password'))
                us.save()
            else:
                return redirect('http://127.0.0.1:8000/list_users/') # użyć reverse
        return HttpResponse("oba hasła muszą być jednakowe")
