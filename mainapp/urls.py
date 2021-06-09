from . import views
from django.contrib import admin
from django.urls import path
app_name = 'mainapp'
urlpatterns = [

    path('', views.firstpage, name='first'),
    path('home/', views.firstpage, name='first'),
    path('intro/', views.intro, name='intro'),
    path('one/', views.project_one, name='project'),
    path('two/', views.project_two, name='project'),
    path('three/', views.project_three, name='project'),
    path('test/', views.test, name='test'),
]

