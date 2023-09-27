from django.urls import path

from tickets import views

urlpatterns = [
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('update_ticket/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
]