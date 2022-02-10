from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('chest', views.chest, name='chest'),
    path('back', views.back, name='back'),
    path('bicep', views.bicep, name='bicep'),
    path('trisep', views.trisep, name='trisep'),
    path('shoulder', views.shoulder, name='shoulder'),
    path('abs', views.abs, name='abs'),
    path('thigh', views.thigh, name='thigh'),
    path('trap', views.trap, name='trap'),


    path('nutrition', views.nutrition, name='nutrition'),
    path('supplement', views.supplement, name='supplement'),
    path('vitamin', views.vitamin, name='vitamin'),
    path('wgain', views.wgain, name='wgain'),
    path('wloss', views.wloss, name='wloss'),
    path('mgain', views.mgain, name='mgain'),


    path('scare', views.scare, name='scare'),
    path('hcare', views.hcare, name='hcare'),
    path('makeup', views.makeup, name='makeup'),
    path('nail', views.nail, name='nail'),



    path('family', views.family, name='family'),
    path('pet', views.pet, name='pet'),
    path('relationship', views.relationship, name='relationship'),
    path('style', views.style, name='style'),
    path('sex', views.sex, name='sex'),
    path('money', views.money, name='money'),
    path('lifehack', views.lifehack, name='lifehack'),



    path('chronicpain', views.chronicpain, name='chronicpain'),
    path('backpain', views.backpain, name='backpain'),
    path('msoreness', views.msoreness, name='msoreness'),
    path('mgproblem', views.mgproblem, name='mgproblem'),
    path('digestive', views.digestive, name='digestive'),
    path('heart', views.heart, name='heart'),
    path('basic', views.basic, name='basic'),













]
