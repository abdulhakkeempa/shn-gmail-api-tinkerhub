import django
from django.shortcuts import redirect, render
from django.http import HttpResponse

from gmail.models import OTP

from .forms import ProjectForm,OTPForm
from .sendOTP import *

# Create your views here.
def homePage(request):
    return render(request,"gmail/webpage_1.html")

def emailPage(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            InputEmail = form['email'].value()
            sendotp(InputEmail,"Django - Test")
            return redirect('otpValidation')
    context = {}
    context['form'] = form
    template = 'gmail/webpage_1.html'
    return render(request,template,context)

def otpPage(request):
    form = OTPForm()
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"gmail/webpage_3.html")
    context = {}
    context ['form'] = form
    return render(request,'gmail/webpage_2.html',context)

