from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.emailPage,name='homePage'),
    path("otp/",views.otpPage,name='otpValidation')
]