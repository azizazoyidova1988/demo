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
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
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
    author_image = models.ImageField(upload_to='images/', blank=True, null=True)
    message = models.CharField(max_length=350, blank=True, null=True)
    description = models.CharField(max_length=450, blank=False, null=False)
    comments = models.IntegerField(blank=False, null=False, default=1)
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
    time = models.CharField(max_length=20, blank=True, null=False)
    guest = models.IntegerField(blank=False, null=False, default=1)

    class Meta:
        db_table = "reservation"

    def __str__(self):
        return self.name


class Contact_User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact_user"

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    job = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.name


class Commenter(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "commentor"

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email


class Image(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "image"

    def __str__(self):
        return self.name
