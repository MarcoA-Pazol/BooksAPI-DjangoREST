from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    #Session URLs
    path('register/', views.register, name='register'),
]
