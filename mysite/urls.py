from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'mysite'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^services/', views.services, name='services'),
    re_path(r'^practivities/', views.practivities, name='practivities'),
    re_path(r'^news/', views.news, name='news'),
    re_path(r'^contact/', views.contact, name='contact')
]
