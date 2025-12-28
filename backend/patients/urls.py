from django.urls import path
from . import views

urlpatterns = [
    #Api part
    path('vitals/', views.patient_vitals, name='vitals'),
    path('medications/', views.patient_medications, name='medications'),
    path('alerts/', views.patient_alerts, name='alerts'),
]
