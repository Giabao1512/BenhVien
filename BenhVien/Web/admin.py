from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse

from .models import *
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'user_type']


class ToaThuocInline(admin.TabularInline):
    model = ToaThuoc.Thuoc.through


class ToaThuocAdmin(admin.ModelAdmin):
    inlines = [ToaThuocInline]


admin.site.register(User, CustomUserAdmin)
admin.site.register(LichTruc)
admin.site.register(Thuoc)
admin.site.register(PhongKham)
admin.site.register(LichKham)
admin.site.register(ToaThuoc, ToaThuocAdmin)
admin.site.register(BenhAn)
admin.site.register(HoaDon)
