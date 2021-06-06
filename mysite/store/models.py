from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    job = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chef"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    comments=models.IntegerField(blank=False,null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.title

class Reservation(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    check_in = models.CharField(max_length=450, blank=False, null=False)
    time = models.TimeField(auto_now=True)
    guest = models.IntegerField(blank=False,null=False,default=1)

    class Meta:
        db_table = "reservation"

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=650, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "about"

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    job = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)