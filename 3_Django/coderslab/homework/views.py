from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product,VAT

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
    def get(self, request, id):
        prod = Product.objects.get(id=id)
        return TemplateResponse(request, 'product.html', context={"id": id})
