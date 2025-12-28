from django.urls import path
from . import views

urlpatterns = [
    # API PART (frontend integration)
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.user_profile, name='profile'),
]
