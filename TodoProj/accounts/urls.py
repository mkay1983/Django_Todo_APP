from django.urls import path

from . import views

urlpatterns = [
    path("user_login/", views.user_login, name='accounts-user_login'),
    path('user_logout/', views.user_logout, name='accounts-user_logout'),
    path('user_register/', views.user_register, name='accounts-user_register'),
]
