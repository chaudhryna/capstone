from django.urls import path

from helpdesk import views

urlpatterns = [
    path('', views.it_dashboard, name='it_dashboard'),
]