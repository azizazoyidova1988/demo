from django.shortcuts import render, redirect
from . import servises
from .models import Reservation, Commenter, User, Contact_User
from store.forms import ReservationForm, CommenterForm, ContactUserForm, UserForm


def home(request):
    model = Reservation()
    form = ReservationForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    a = 'Far far away, behind the word mountains, ' \
        'far from the countries Vokalia and Consonantia,' \
        ' there live the blind texts. Separated they live ' \
        'in Bookmarksgrove right at the coast of the ' \
        'Semantics, a large language ocean.'
    var = [{
        "image1": '../static/taste_it/images/bg_6.jpg',
        'image2': '../static/taste_it/images/bg_4.jpg',
        'title': 'Perfect Ingredients',
        "desc": a
    }]

    customer = servises.get_customer()
    chefs = servises.get_chefs()
    blog = servises.get_blog()
    categories = servises.get_categories()
    products = servises.get_products()

    ctx = {

        "customer": customer,
        "chefs": chefs,
        "blog": blog,
        "categories": categories,
        "products": products,
        'var':var,
        "home_page": 'active'
    }
    return render(request, 'taste_it/index.html', ctx)


def about(request):
    a = 'Far far away, behind the word mountains, ' \
        'far from the countries Vokalia and Consonantia,' \
        ' there live the blind texts. Separated they live ' \
        'in Bookmarksgrove right at the coast of the ' \
        'Semantics, a large language ocean.'
    var = [{
        "image1": '../static/taste_it/images/bg_6.jpg',
        'image2': '../static/taste_it/images/bg_4.jpg',
        'title': 'Perfect Ingredients',
        "desc": a
    }]

    customer = servises.get_customer()
    ctx = {

        "customer": customer,
        "about_page": "active",
        'var': var,
        "blog_single": blog_single
    }
    return render(request, 'taste_it/about.html', ctx)


def menu(request):
    model = Reservation()
    form = ReservationForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    categories = servises.get_categories()
    products = servises.get_products()
    ctx = {

        "categories": categories,
        "products": products,
        "menu_page": "active"
    }

    return render(request, 'taste_it/menu.html', ctx)


def chef(request):
    model = Reservation()
    form = ReservationForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    chefs = servises.get_chefs()
    ctx = {
        "chefs": chefs,
        "chef_page": "active"
    }
    return render(request, 'taste_it/chef.html', ctx)


def reservation(request):
    model = Reservation()
    form = ReservationForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    a = 'Far far away, behind the word mountains, ' \
        'far from the countries Vokalia and Consonantia,' \
        ' there live the blind texts. Separated they live ' \
        'in Bookmarksgrove right at the coast of the ' \
        'Semantics, a large language ocean.'
    var = [{
        "image1": '../static/taste_it/images/bg_6.jpg',
        'image2': '../static/taste_it/images/bg_4.jpg',
        'title': 'Perfect Ingredients',
        "desc": a
    }]

    ctx = {

        "reservation_page": "active",
        "var": var

    }
    return render(request, 'taste_it/reservation.html', ctx)


def blog(request):
    blog = servises.get_blog()
    ctx = {
        "blog": blog,
        "blog_page": "active"
    }
    return render(request, 'taste_it/blog.html', ctx)


def blog_single(request, blog_id):
    model = Commenter()
    form = CommenterForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    blog = servises.get_blog()
    blog_single = servises.get_blog_single(blog_id=blog_id)
    customer = servises.get_customer()
    category_count = servises.get_categories_product_count()

    ctx = {
        "blog": blog,
        "blog_single": blog_single,
        "customer": customer,
        "category_count": category_count
    }
    return render(request, 'taste_it/blog-single.html', ctx)


def contact(request):
    model = Contact_User()
    form = ContactUserForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        "contact_page": "active"
    }
    return render(request, 'taste_it/contact.html', ctx)


# def email(request):
#     model = User()
#     form = UserForm(request.POST or None, instance=model)
#     if request.POST:
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             print(form.errors)
#     return render(request, 'taste_it/footer.html')


