from django.urls import path
from . import views

from .views import VerificationView 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views


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
    path("helpline_numbers/", views.helpline_numbers, name="helpline_numbers"),
    path("women_laws/", views.women_laws, name="women_laws"),
    path('women_rights/', views.women_rights, name='women_rights'),
    path('ngo_details/', views.ngo_details, name='ngo_details'),
    path("developers/", views.developers, name="developers"),
    path('contact_user/', views.contact_user , name="contact_user"),
    path("404_error/", views.page_not_found, name="404_error"),        
    path("activate/<uidb64>/<token>", VerificationView.as_view() ,name= "activate"),      
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "main_app/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="main_app/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="main_app/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main_app/password_reset_done.html"), name="password_reset_complete"),
              ]


