from django.urls import path

from helpdesk import views

urlpatterns = [
    path('tech-chart/', views.tech_chart, name='tech_chart'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('', views.it_dashboard, name='it_dashboard'),
]

