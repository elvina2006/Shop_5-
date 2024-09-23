from allauth.account.forms import SignupForm
from django import forms


class CustomUserForm(SignupForm):
    age = forms.IntegerField(label='Возраст')
    country = forms.CharField(max_length=100, label='Город')
    phone_number = forms.CharField(max_length=15, required=False, label='Телефон номер')
