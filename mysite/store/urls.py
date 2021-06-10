from django.urls import path, include
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('chef/', views.chef, name='chef'),
    path('reservation/', views.reservation, name='reservation'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/blog_single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', include('dashboard.urls'))

]
