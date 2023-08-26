from django.contrib import admin
from django.urls import path, include 

from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', accounts_views.dashboard, name='dashboard'),
]
