from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logs/', views.time_logs, name='time_logs'),
    path('manual-entry/', views.manual_entry, name='manual_entry'),
    path('save-time-log/', views.save_time_log, name='save_time_log'),
]