from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #Session URLs
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('protected_view/', views.ProtectedView.as_view(), name='protected-view'),
]
