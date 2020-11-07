from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('emergency_contact/', views.emergency_contact, name="emergency_contact"),
    path("create_contact/", views.create_contact , name="create_contact"),
    path("update_contact/<str:pk>/", views.update_contact, name="update_contact"),
    path("delete_contact/<str:pk>/", views.delete_contact, name="delete_contact"),
    path("emergency/", views.emergency, name="emergency"),
    path("helpline_numbers/", views.helpline_numbers, name="helpline_numbers")
              ]