from django.urls import path

from invoicegen import views

urlpatterns = [
    path('', views.invoice_send)
]