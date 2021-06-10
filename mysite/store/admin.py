from django.contrib import admin
from .models import Chef, Category, Customer, Product, User, Reservation, \
    Blog, Commenter, Contact_User,Image

admin.site.register(Chef)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Commenter)
admin.site.register(Contact_User)
admin.site.register(Image)
