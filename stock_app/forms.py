from django import forms
from django.contrib.auth.forms import UserCreationForm

from stock_app.models import Login, register, stock


class Login_form(UserCreationForm):
    class Meta :
        model=Login
        fields = ("username","password1",'password2')



class register_form1(forms.ModelForm):
    class Meta:
         model = register
         fields = '__all__'
         exclude = ("user",)



class StockForm(forms.ModelForm):
    class Meta:
         model = stock
         fields = '__all__'

