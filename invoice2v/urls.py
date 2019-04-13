from django.contrib import admin
from django.urls import path

from invoice2v import views

urlpatterns = [
    path('', views.invoice_send)
]
