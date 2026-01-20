from django.urls import path
from .views import linux_home, windows_home
from portfolio import views

urlpatterns = [
    path("", linux_home, name="linux_home"),
    path("windows/", windows_home, name="windows_home"),
    path("contact-send/", views.contact_send_email, name="contact_send_email")
]
