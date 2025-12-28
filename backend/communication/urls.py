from django.urls import path
from .viwes import chat_history, call_logs

urlpatterns = [
    #Api part
    path('chat/', chat_history),
    path('calls/', call_logs),
]
