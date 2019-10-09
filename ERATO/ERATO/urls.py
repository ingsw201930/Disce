"""ERATO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from app_sessions import views as session_views
from app_sw import views as sw_views
from app_client import views as client_views
from app_date import views as date_views

urlpatterns = [
    path('admin/', admin.site.urls),

#   SESSIONS
    path('',session_views.main_,name='main'),
    path('sessions_managing_login/',session_views.login_managing,name='login'),
    path('login/c/', auth_views.LoginView.as_view(template_name='login_c/login.html') , name="login_c"),
    path('login/s/', auth_views.LoginView.as_view(template_name='login_s/login.html') , name="login_s"),
    path('logout/', session_views.logout_managing),

#   Sw functionalities
    path('home/s/', sw_views.home_s , name="home_s"),
    path('service_add_request/', sw_views.service_add_form , name="service_add"),
    path('service_add_request/service_adding_service/', sw_views.service_add , name="service_add"),
    path('service_del/<int:service_id>', sw_views.service_del , name="service_del"),
    path('service_edit/<int:service_id>', sw_views.service_edit_form , name="service_edit"),
    path('date_by_service/<int:service_id>',date_views.date_by_service,name="date_by_service"),
    path('profile/s/<int:sw_id>',sw_views.public_profile,name="sw_public_profile"),

    path( 'date_form/<int:service_id>', date_views.date_form, name="form" ),

#   Client functionalities
    path('home/c/', client_views.home_c , name="home_c"),
    path('profile/c/<int:client_id>',client_views.public_profile,name="client_public_profile"),

#   QR
    path('generate_date/<int:service_id>', date_views.generate_date, name="generate_date"),
    path('createQR/<int:date_id>',date_views.createQR),
    path('QRcheck/<int:id>/<str:code>',date_views.checkQR),
    path('signup/s/',sw_views.signup,name="signup_s"),
    path('signup/c/',client_views.signup,name="signup_c"),
    path('accept_date/<int:date_id>',date_views.accept_date,name='accept_date'),

]
