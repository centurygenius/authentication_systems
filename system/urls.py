from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('logout/', views.logoutUser, name='logout'),
]
