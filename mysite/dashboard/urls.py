from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('customer/list/', views.customers_list, name="customers_list"),
    path('customer/add/', views.customers_create, name="customers_add"),
    path('customer/<int:customer_id>/edit/', views.customers_edit, name="customers_edit"),
    path('customer/<int:customer_id>/delete/', views.customers_delete, name="customers_delete"),

    path('category/list/', views.categories_list, name="categories_list"),
    path('category/add/', views.categories_create, name="categories_add"),
    path('category/<int:category_id>/edit/', views.categories_edit, name="categories_edit"),
    path('category/<int:category_id>/delete/', views.categories_delete,name="categories_delete"),

    path('product/list/', views.products_list, name="products_list"),
    path('product/add/', views.products_create, name="products_add"),
    path('product/<int:product_id>/edit/', views.products_edit, name="products_edit"),
    path('product/<int:product_id>/delete/', views.products_delete, name="products_delete"),

    path('chef/list/', views.chefs_list, name="chefs_list"),
    path('chef/add/', views.chefs_create, name="chefs_add"),
    path('chef/<int:chef_id>/edit/', views.chefs_edit, name="chefs_edit"),
    path('chef/<int:chef_id>/delete/', views.chefs_delete, name="chefs_delete"),

   ]