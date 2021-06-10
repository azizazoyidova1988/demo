from django import forms
from store.models import Reservation, Commenter, Product, Chef, Customer, Category,User,Contact_User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation()
        fields = '__all__'


class CommenterForm(forms.ModelForm):
    class Meta:
        model = Commenter()
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer()
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = '__all__'


class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef()
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = '__all__'

class ContactUserForm(forms.ModelForm):
    class Meta:
        model = Contact_User()
        fields = '__all__'
