from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("business/", views.business, name='business'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact')
]
