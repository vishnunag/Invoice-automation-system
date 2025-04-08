from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_clients, name='upload_clients'),
    path('clients/', views.client_list, name='client_list'),
    path('send/<int:client_id>/', views.send_invoice, name='send_invoice'),
]