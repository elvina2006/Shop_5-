from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import UserProfile



class CustomUserForm(SignupForm):
    age = forms.IntegerField(label='Возраст')
    country = forms.CharField(max_length=100, label='Город')
    phone_number = forms.CharField(max_length=15, required=False, label='Телефон номер')




def clean_phone_number(self):
    phone_number = self.cleaned_data.get('phone_number')
    if phone_number and len(phone_number) != 9:
        raise forms.ValidationError("Номер телефона должен состоять из 9 символов.")
    return phone_number


def save(self, request):
    user = super(CustomUserForm, self).save(request)
    phone_number = self.cleaned_data['phone_number']
    user.phone_number = "+996" + phone_number
    user.age = self.cleaned_data['age']
    user.country = self.cleaned_data['country']
    user.save()
    return user


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Category)
admin.site.register(ProductPhotos)
admin.site.register(Comment)
admin.site.register(UserProfile)

