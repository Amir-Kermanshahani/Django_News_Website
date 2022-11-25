from django.urls import path
from django.urls import reverse_lazy
from . import views 


app_name = 'authapp'

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),

    path('', views.signin, name='login'),

    path('logout/', views.signout, name='logout'),


]   