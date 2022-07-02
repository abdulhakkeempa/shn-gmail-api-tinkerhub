from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.emailPage),
    path("otp/",views.otpPage,name='otpValidation')
]