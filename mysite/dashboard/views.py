from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from store.models import Commenter, Customer, Chef, Category, Product, \
    Reservation, Blog
from store.forms import *
from . import servises


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    category = servises.get_categories_count()
    products_count = servises.get_products_count()
    chefs_count = servises.get_chefs_count()
    customers_count = servises.get_customers_count()
    category_product=servises.get_categories_products_count()


    ctx = {
        "category": category,
        "products_count":  products_count,
        "chefs_count": chefs_count,
        "customers_count": customers_count,
        "category_product": category_product,


    }
    return render(request, 'dashboard/index.html',ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def categories_list(request):
    categories = servises.get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
def categories_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def categories_edit(request, category_id):
    model = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)

@login_required_decorator
def categories_delete(request, category_id):
    model = Category.objects.get(id=category_id)
    model.delete()
    return redirect("categories_list")

@login_required_decorator
def customers_list(request):
    customers = servises.get_customer()
    ctx = {
        "customers": customers
    }
    return render(request, 'dashboard/customer/list.html', ctx)

@login_required_decorator
def customers_create(request):
    model = Customer()
    form = CustomerForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('customers_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/customer/form.html', ctx)

@login_required_decorator
def customers_edit(request, customer_id):
    model = Customer.objects.get(id=customer_id)
    form = CustomerForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('customers_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/customer/form.html', ctx)

@login_required_decorator
def customers_delete(request, customer_id):
    model = Customer.objects.get(id=customer_id)
    model.delete()
    return redirect("customers_list")

@login_required_decorator
def chefs_list(request):
    chefs = servises.get_chefs()
    ctx = {
        "chefs": chefs
    }
    return render(request, 'dashboard/chef/list.html', ctx)

@login_required_decorator
def chefs_create(request):
    model = Chef()
    form = ChefForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('chefs_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/chef/form.html', ctx)

@login_required_decorator
def chefs_edit(request, chef_id):
    model = Chef.objects.get(id=chef_id)
    form = ChefForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('chefs_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/chef/form.html', ctx)

@login_required_decorator
def chefs_delete(request, chef_id):
    model = Chef.objects.get(id=chef_id)
    model.delete()
    return redirect("chefs_list")

@login_required_decorator
def products_list(request):
    products = servises.get_products()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)

@login_required_decorator
def products_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)

@login_required_decorator
def products_edit(request, product_id):
    model = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)

@login_required_decorator
def products_delete(request, product_id):
    model = Product.objects.get(id=product_id)
    model.delete()
    return redirect("products_list")
