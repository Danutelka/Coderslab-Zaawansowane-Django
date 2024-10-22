from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product,VAT
from .forms import AddCategoryForm, EditCategoryForm, EditProductForm, SearchForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import django.contrib.auth.decorators
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
# dzien 1 zad 2
class CategoriesView(View):
    def get (self, request):
        kat = Category.objects.all().order_by('category_name')
        return TemplateResponse(request, 'categories.html', context={"kat": kat})

# dzien 1 zad 3
class CategorySlugView(View):
    def get (self, request, x):
        a = Category.objects.get(slug=x)
        b = Product.objects.filter(categories=a.id).order_by('name')
        return TemplateResponse(request, 'slug.html', context={"a": a, "b": b})

# dzien 1 zad 4
class ProductView(View):
    def get(self, request, pk):
        prod = get_object_or_404(Product, id=pk)
        context ={
            "prod": prod
        }
        return TemplateResponse(request, 'product.html', context)

# dzien 2 zad 5
class AddCategoryView(PermissionRequiredMixin, View):
    permission_required = "auth.add_category"
    def get(self, request):
        form = AddCategoryForm()
        return TemplateResponse(request, 'add_category.html', {'form':form})
    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            slug = form.cleaned_data['slug']
            Category.objects.create(category_name=category_name, slug=slug)
            return HttpResponseRedirect("categories")

class EditCategoryView(PermissionRequiredMixin, View):
    permission_required = "auth.change_category"
    def get(self, request, s):
        form = EditCategoryForm()
        sl = Category.objects.get(slug=s)
        return TemplateResponse(request, 'edit_category.html', context={'form': form, 'sl': sl})
    def post(self, request, s):
        form = EditCategoryForm(request.POST)
        sl = Category.objects.get(slug=s)
        if form.is_valid():
            sl.category_name = form.cleaned_data['category_name']
            sl.slug = form.cleaned_data['slug']
            sl.save()
            return HttpResponseRedirect("categories")

# dzien 2 zad 6
class ProductsView(View):
    def get(self, request):
        pr = Product.objects.all().order_by('name')
        return TemplateResponse(request, "products.html", context={'pr': pr})

class EditProductView(PermissionRequiredMixin, View):
    permission_required = "auth.change_product"
    def get(self, request, p):
        form = EditProductForm()
        pro = Product.objects.get(id=p)
        return TemplateResponse(request, 'edit_product.html', context={'form': form, 'pro': pro})
    def post(self, request, p):
        form = EditProductForm(request.POST)
        pro = Product.objects.get(id=p)
        if form.is_valid():
            pro.name = form.cleaned_data['name']
            pro.description = form.cleaned_data['description']
            pro.price = form.cleaned_data['price']
            pro.vat = form.cleaned.data['vat']
            pro.stock = form.cleaned.data['stock']
            pro.categories = form.cleaned.data['categories']
            pro.save()
            return HttpResponseRedirect("products")

class ProductCreate(PermissionRequiredMixin, CreateView):
    permission_required = "auth.add_product"
    model = Product
    fields = '__all__'
    success_url = "products"

#dzien 2 / zad 7*
class SearchView(View):
    def get(self, request):
        form = SearchForm()
        return TemplateResponse(request, 'search.html', context={'form': form})
    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            product = Product.objects.filter(name__icontains=name)
            category = Category.objects.filter(category_name__icontains=name)
            context = {
                "form": form,
                "product": product,
                "category": category
            }
        return TemplateResponse(request, "search.html", context=context)

#dzien 3 / zad 8
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
                return HttpResponseRedirect("products")
            else:
                return HttpResponse('ups niepoprawne logowanie')
        return render(request, 'login2.html', context={'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')