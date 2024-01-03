from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path("addjob/", views.addjob, name="addjob"),  # Corrected to "addjob"
    path("alljob/", views.alljob, name="alljob"),  # Corrected to "alljob"
    path("stats/", views.stats, name="stats"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.user_logout, name="logout"),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('update/<str:id>/', views.jobupdate, name='update'),


]
