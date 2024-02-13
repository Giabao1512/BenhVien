# from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('LichKham', views.LichKhamView)
router.register('ToaThuoc', views.ToaThuocView)
router.register('BenhAn', views.BenhAnView)
urlpatterns = [
    path('', include(router.urls)),
]
