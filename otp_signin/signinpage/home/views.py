from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password


# Create your views here.
def home(request):
    return render(request,"home.html")

def signin_verification(request):
     if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        request.session["username"]=username
        request.session["password"]=password1
        request.session["email"]=email
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('signin')
            else:
                send_otp(request)
                return render(request,'otp.html',{"email":email})
        else:
            messages.info(request,"password mismatch")
            return redirect("signin")

def send_otp(request):
    s=""
    for x in range(0,4):
        s+=str(random.randint(0,9))
    request.session["otp"]=s
    send_mail("otp for sign up",s,'djangoalerts0011@gmail.com',[request.session['email']],fail_silently=False)
    return render(request,"otp.html")

def  otp_verification(request):
    if  request.method=='POST':
        otp_=request.POST.get("otp")
    if otp_ == request.session["otp"]:
        encryptedpassword=make_password(request.session['password'])
        nameuser=User(username=request.session['username'],email=request.session['email'],password=encryptedpassword)
        nameuser.save()
        messages.info(request,'signed in successfully...')
        User.is_active=True
        return redirect('home')
    else:
        messages.error(request,"otp doesn't match")
        return render(request,'otp.html')