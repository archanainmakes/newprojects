from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('signin_verification',views.signin_verification,name="signin_verification"),
    path('otp_verification',views.otp_verification,name="otp_verification")
]