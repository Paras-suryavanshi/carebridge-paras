from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # app routes
    path('api/users/', include('users.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/communication/', include('communication.urls')),
]
