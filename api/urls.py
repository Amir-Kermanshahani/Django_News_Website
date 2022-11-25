from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.views.generic import TemplateView


urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('single/<slug:slug>/', views.Single.as_view(), name='single'),
    path('category/<str:cat>/', views.CategoryView.as_view(), name='category'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)