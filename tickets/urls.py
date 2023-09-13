from django.urls import path

from tickets import views

urlpatterns = [
    path('create_ticket/', views.create_ticket, name='create_ticket'),
]