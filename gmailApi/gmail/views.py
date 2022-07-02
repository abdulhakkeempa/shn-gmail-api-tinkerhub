import django
from django.shortcuts import redirect, render
from django.http import HttpResponse

#from gmail.models import OTP

from .forms import ProjectForm,OTPForm
from .sendOTP import *

# Create your views here.
def homePage(request):
    return render(request,"gmail/webpage_1.html")

global ret_otp

def emailPage(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            InputEmail = form['email'].value()
            global ret_otp
            ret_otp = sendotp(InputEmail,"Django - Test")
            return redirect('otpValidation')
    context = {}
    context['form'] = form
    template = 'gmail/webpage_1.html'
    return render(request,template,context)


def checkOTP(userOTP,ret_otp):
    if userOTP == ret_otp:
        return True
    else:
        return False


def otpPage(request):
    form = OTPForm()
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            form.save()
            userOTP = form['otp'].value()
            if checkOTP(userOTP,ret_otp):
                return render(request,"gmail/webpage_3.html")
            else:
                return HttpResponse("Sorry Invalid OTP")
    context = {}
    context ['form'] = form
    return render(request,'gmail/webpage_2.html',context)

