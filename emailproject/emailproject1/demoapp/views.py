from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        send_mail(
            #subject
            "testing",
            #message
            content,
            #from email
            settings.EMAIL_HOST_USER,
            #recipent list
            [to]
        )
        return render(
        request,
        'email.html',
        {
        'title':'send an email'
        }
    )
    else:
        return render(
        request,
        'email.html',
        {
        'title':'send an email'
        }
    )
