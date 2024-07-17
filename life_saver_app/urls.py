from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forgot', views.forgot, name='forgot'),
    path('pwdupdate', views.pwdupdate, name='pwdupdate'),
    path('save_for', views.save_for, name='save_for'),
    path('home', views.home, name='home'),
    path('help', views.help, name='help'),
    path('certificate', views.certificate, name='certificate'),
]